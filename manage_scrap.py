from app.main.src.google_map_scrapper import GoogleMapScrapper
from app.main.config import DevelopmentConfig

def main():
    GoogleMapScrapper(
        DevelopmentConfig.SQLALCHEMY_DATABASE_URI, 
        localisation="paris", 
        keyword="vetements", 
        page_result=2
    )


if __name__ == "__main__":
    main()