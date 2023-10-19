import requests
import pandas

url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
dateModified = '2022-02-07 14:03' 

def main():
    # your code here
    # get html page
    page = requests.get(url).text.split('<tr>')
    # remove the first row which is the header
    page.pop(0)
    # find the filename that contains the dateModified
    fileUrl = ''
    for row in page:
        if dateModified in row:
            filename = row.split('"')[1]
            fileUrl = url + filename
            break
    # download the file and load into pandas dataframe
    df = pandas.read_csv(fileUrl)
    # find the records that has the highest HourlyDryBulbTemperature
    maxTemp = df['HourlyDryBulbTemperature'].max()

    # print the record(s)
    print(df.loc[df['HourlyDryBulbTemperature'] == maxTemp])

    pass


if __name__ == "__main__":
    main()
