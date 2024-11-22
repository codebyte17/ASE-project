
#currentWorkingDirectory = "D:\AdvanceSoftwareEngineeringTask\ASE\\berlingeoheatmap_project1"
#currentWorkingDirectory = "/mount/src/berlingeoheatmap1/"

# -----------------------------------------------------------------------------
import os
#os.chdir(currentWorkingDirectory)
print("Current working directory\n" + os.getcwd())

import pandas                        as pd
from core import methods             as m1
from core import HelperTools         as ht

from config                          import pdict

# -----------------------------------------------------------------------------
@ht.timer
def main():
    """Main: Generation of Streamlit App for visualizing electric charging stations & residents in Berlin"""
# Load datasets

    ladesaeulen_file = "D:/BHT-university/advanced software engineering-Fortgeschrittene Softwaretechnik/project/berlingeoheatmap_project1/Ladesaeulenregister.csv"
    residents_file = "D:/BHT-university/advanced software engineering-Fortgeschrittene Softwaretechnik/project/berlingeoheatmap_project1/plz_einwohner.csv"

    # Reading GeoDataFrame for PLZ geometries
    df_geodat_plz = pd.read_csv("datasets/geodata_berlin_plz.csv", sep=';', encoding='utf-8')

    # Reading electric charging stations data
    df_lstat = pd.read_csv("datasets/Ladesaeulenregister.csv", sep=';', skiprows=10, encoding='utf-8', low_memory=False)

    # Reading residents data
    df_residents = pd.read_csv("datasets/plz_einwohner.csv", sep=',', encoding='utf-8') 

    # Preprocessing electric charging stations
    df_lstat2 = m1.preprop_lstat(df_lstat, df_geodat_plz, pdict)
    gdf_lstat3 = m1.count_plz_occurrences(df_lstat2)

    # Preprocessing residents data
    gdf_residents2 = m1.preprop_resid(df_residents, df_geodat_plz, pdict)

    # Generate Streamlit app with heatmaps
    m1.make_streamlit_electric_Charging_resid(gdf_lstat3, gdf_residents2)
        
# -----------------------------------------------------------------------------------------------------------------------

    #


if __name__ == "__main__": 
    main()

