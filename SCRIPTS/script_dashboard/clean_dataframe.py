import pandas as pd
import functions_dashboard as fd
from PIL import Image

# 1. Google drive directory of each team member
#directory_aurelien =
#directory_alexandre =
#directory_marion =
#directory_mohammed =

# 2. Declare csv clean directories
link_title_akas_clean = "csv_clean/title_akas_clean.csv"
link_title_basics_clean = "csv_clean/title_basics_clean.csv"
link_title_genre_clean = "csv_clean/title_genre_clean.csv"
link_name_basics_clean = "csv_clean/title_nameBasics_clean.csv"
link_name_basics_keys = "csv_clean/title_nameBasics_clean.csv"
link_title_principals_clean = "csv_clean/title_principals_clean.csv"
link_title_rating_clean = "csv_clean/title_ratings_clean.csv"

# 3. Generate dataframe from custom function
df_title_akas_clean = fd.read_database(link_title_akas_clean, ",")
df_title_basics_clean = fd.read_database(link_title_basics_clean, ",")
df_title_genre_clean = fd.read_database(link_title_genre_clean, ",")
df_name_basics_clean = fd.read_database(link_name_basics_clean, ",")
df_name_basics_keys = fd.read_database(link_name_basics_keys, ",")
df_title_principals_clean = fd.read_database(link_title_principals_clean, ",")
df_title_rating_clean = fd.read_database(link_title_rating_clean, ",")

# 4. import dashboard image
link_dashboard_picture = "cinema.jpg"
dashboard_img = Image.open(link_dashboard_picture)

