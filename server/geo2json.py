def geo2json(geofile, jsonfile):
    out = open(jsonfile, "w")
    out.write('''
{
    "type": "FeatureCollection",
    "features": [
    ''')
    with open(geofile) as f:
        f.readline()  # 丢掉第一行表头
        while True:
            line = f.readline()
            if line == "":
                break

            geo_id = int(line.split(',')[0])
            coordinates = line.split('"')[1]
            s = '''
{
    "type": "Feature",
    "geometry": {
        "type": "LineString",
        "coordinates": %s
    },
    "properties": {
        "geo_id": %d
    }
}''' % (coordinates, geo_id)
            out.write(s)
            out.write(',')
    out.seek(out.tell()-1,0) # 把多余的逗号删掉
    out.write('''\t]\n}''')
    out.close()


if __name__ == '__main__':
    geofile = 'raw_data/porto_roadmap_edge/porto_roadmap_edge.geo'
    jsonfile = 'raw_data/tmp/my.json'
    geo2json(geofile, jsonfile)
