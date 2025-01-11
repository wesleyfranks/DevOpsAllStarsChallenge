import os 
import json
import boto3
import requests
from datetime import datetime
from dotenv import load_dotenv
import argparse

# Load environment variables
load_dotenv()

class Weather_Dashboard:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.bucket_name = os.getenv('AWS_BUCKET_NAME')
        self.s3_client = boto3.client('s3')

    def create_bucket_if_not_exists(self):
        """Create S3 bucket if it doesn't exist"""
        try:
            self.s3_client.head_bucket(Bucket=self.bucket_name)
            print(f"Bucket {self.bucket_name} exists")
        except:
            print(f"Creating bucket {self.bucket_name}")
        try: 
            # Simpler creation for us-east-1
            self.s3_client.create_bucket(Bucket=self.bucket_name)
            print(f"Successfully created bucket {self.bucket_name}")
        except Exception as e:
            print(f"Error creating bucket: {e}")

    def delete_bucket(self):
        """Delete S3 bucket"""
        try:
            # List all objects in the bucket
            objects = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' in objects:
                for obj in objects['Contents']:
                    self.s3_client.delete_object(Bucket=self.bucket_name, Key=obj['Key'])
                    print(f"Deleted {obj['Key']} from {self.bucket_name}")
                
            # Delete bucket
            self.s3_client.delete_bucket(Bucket=self.bucket_name)
            print(f"Successfully deleted bucket {self.bucket_name}")
        except Exception as e:
            print(f"Error deleting bucket: {e}")

    def fetch_weather(self, city):
        """Fetch weather data from OpenWeather API"""
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "imperial"
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def save_to_s3(self, weather_data, city): 
        """Save weather data to S3 bucket"""
        if not weather_data:
            return False
        
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        file_name = f"weather-data/{city}-{timestamp}.json"

        try: 
            weather_data['timestamp'] = timestamp
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=json.dumps(weather_data),
                ContentType='application/json'
            )
            print(f"Successfully saved {file_name} to S3")
            return True 
        except Exception as e: 
            print(f"Error saving to S3: {e}")
            return False

def main(action): 
    dashboard = Weather_Dashboard()

    if action == "delete":
        dashboard.delete_bucket()
        return
    if action == "run" or action == "":
        dashboard.create_bucket_if_not_exists()

        cities = ["Houston", "Austin", "Dallas"]

        for city in cities: 
            print(f"\nFetching weather for {city}...")
            weather_data = dashboard.fetch_weather(city)
            if weather_data:
                temp = weather_data['main']['temp']
                feels_like = weather_data['main']['feels_like']
                humidity = weather_data['main']['humidity']
                description = weather_data['weather'][0]['description']

                print(f"Temperature: {temp}°F")
                print(f"Feels like: {feels_like}°F")
                print(f"Humidity: {humidity}%")
                print(f"Conditions: {description}")

                # Save to S3
                success = dashboard.save_to_s3(weather_data, city)
                if success: 
                    print(f"Weather data for {city} saved to S3")
            else: 
                print(f"Failed to fetch weather data for {city}")
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Weather Dashboard")
    parser.add_argument("action", nargs='?', default="run", choices=["","run","delete"], help="Action to perform")
    args = parser.parse_args()
    
    main(args.action)