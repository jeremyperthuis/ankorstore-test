import re
from time import sleep

import pandas as pd
from sqlalchemy import create_engine
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from app.main import log_datahandler




class GoogleMapScrapper:
    """
        Scrap Google maps to retrieve business info
        take three arguments : 
            - localisation : place like city or region (ex : Paris)
            - keyword : type of business like "garage" or "retail"
            - page_result : number of page result to crawl (2O results per page)
    """
    google_map_url = "https://www.google.com/maps/place/"
    driver = webdriver.Chrome(ChromeDriverManager().install())
   
    business_df = pd.DataFrame()
    def __init__(self,db_uri=None, localisation=None, keyword=None, page_result=1):
        self.search(localisation=localisation, keyword=keyword)
        self.retrieve_results(page_result=page_result)
        self.driver.close()
        self.cleaning_data()
        self.persistence_to_sql(self.business_df, db_uri)

    
    def persistence_to_sql(self, df, db_uri):
        try:
            db = create_engine(db_uri)
            db.connect()
            df.to_sql(con=db, name="company", if_exists='append', index=False)
            log_datahandler.info("{} row(s) saved into database.".format(df.shape[0]))
        except Exception as e:
            log_datahandler.error(e)

    def search(self, localisation, keyword):
        self.driver.get(f"{self.google_map_url}{localisation}")
        if "consent.google" in str(self.driver.current_url):
            accept_button = self.driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button")
            accept_button.click()
        sleep(8)
        searchbar = self.driver.find_element_by_class_name("tactile-searchbox-input")
        searchbar.clear()
        sleep(3)
        searchbar.send_keys(f"{keyword}")
        submit = self.driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
        submit.click()
        sleep(5)
    
    def retrieve_results(self, page_result=1):
        for i in range(page_result):
            self.scroll_gmaps_results(scrolling_amount=6)
            results_pane = self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]")
            res = results_pane.find_elements_by_xpath("./*")
            for elem in res:
                if elem.text:
                    raw_str = elem.text.replace("\n", "??")
                    raw_list = raw_str.split("??")
                    raw_list = list(filter(None, raw_list))
                    self.business_df = self.business_df.append(
                            {
                                "name":raw_list.pop(0), 
                                "score":raw_list.pop(0),
                                "type":raw_list.pop(0),
                                "address":raw_list.pop(0),
                                "others_info":raw_list,

                            },ignore_index=True)

            sleep(6)
            if page_result > 1 :
                next_button = self.driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/button[2]")
                next_button.click()
                sleep(6)

    def cleaning_data(self):
        # Score cleaning
        split_score = self.business_df["score"].str.split("(", n=1, expand=True)
        self.business_df["google_score"] = split_score[0]
        self.business_df["google_review_count"] = split_score[1]
        self.business_df['google_review_count'] = self.business_df['google_review_count'].str.replace(')','')
        self.business_df.drop(["score"], axis=1, inplace=True)
        
        # Phone number cleaning
        def getphonenumber(row):
            other_info = row['others_info']
            temp = [s.strip() for s in other_info]
            phone_regex = re.compile("[\d ]{10,16}")
            result = list(filter(phone_regex.match, temp))
            if len(result):
                return result[0].replace(" ","")
            else: 
                return None
        
        self.business_df["telephone_number"] = self.business_df.apply(getphonenumber, axis=1)
        self.business_df.drop(["others_info"], axis=1, inplace=True)
            
    def scroll_gmaps_results(self, scrolling_amount=1):
        for i in range(scrolling_amount):
            scroll = self.driver.find_elements(By.CSS_SELECTOR, '.TFQHme')
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll[-1])
            sleep(3)


