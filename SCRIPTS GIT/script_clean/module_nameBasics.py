import pandas as pd
import functions_clean as fc
import module_table_titlebasics as mttb
import constant as ct




def title_nameBasics(link):

    # Load of title_principals table in a DF, which is df_to_clean
    df_title_nameBasics = fc.read_database(link, "\t")
    # decompose title basics
    #Put column 'knowForTitles in List type:

    df_title_nameBasics['knownForTitles'] = df_title_nameBasics.knownForTitles.str.split( "," ,
                                                                                                      expand = False )
    #Explode df_title_nameBasic from column KnowForTitle:

    df_title_nameBasics = df_title_nameBasics.explode( column = 'knownForTitles' ,
                                                          ignore_index = True )
    # Rename columns KnowForTitle par tconst

    df_title_nameBasics.rename( columns = {'knownForTitles': 'tconst'} , inplace = True )
    # Apply of clean_rows function

    df_title_nameBasics_clean = fc.clean_rows( df_title_nameBasics, mttb.title_basics_clean , 'tconst' )
    #Select first tables df_title_nameBasics and df_title_nameBasics

    title_nameBasics_key=df_title_nameBasics_clean.loc[: , ['nconst' , 'tconst']]
    title_nameBasics=df_title_nameBasics_clean.iloc[:,0:4]

    #Delelte dublicate rows in df_nameBsaics

    title_nameBasics= title_nameBasics.drop_duplicates()
    title_nameBasics = title_nameBasics.reset_index( drop = True )
    #Delete columns birth and die dates:

    title_nameBasics= title_nameBasics.iloc[: , 0:2]
    return (title_nameBasics,title_nameBasics_key)

title_nameBasics_clean,title_nameBasics_keys=title_nameBasics(ct.link_name_basics)

# Export csv file from df_title_principals_clean
title_nameBasics_clean.to_csv (f"{ct.directory_aurelien}title_nameBasics_clean.csv", sep = ",", index = False)
title_nameBasics_keys.to_csv (f"{ct.directory_aurelien}title_nameBasics_keys.csv", sep = ",", index = False)
