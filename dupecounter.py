import csv, argparse, time, datetime

dupe_original = 0
dupe_matched = 1
dupe_filesize = 2
dupe_hash = 3

dupecount = {}

def dupecounter(dupecsvfile, dupecountfile):
    with open(dupecsvfile, "r") as dupefile:
        dupereader = csv.reader(dupefile)
        
        for dupe in dupereader:
            if dupe[dupe_original] not in dupecount:
                dupecount[dupe[dupe_original]] = {}
                dupecount[dupe[dupe_original]]["count"] = 0
                dupecount[dupe[dupe_original]]["filesize"] = dupe[dupe_filesize]
                dupecount[dupe[dupe_original]]["hash"] = dupe[dupe_hash]
            else:
                dupecount[dupe[dupe_original]]["count"] += 1

        with open(dupecountfile, "w") as countfile:
            countwriter = csv.writer(countfile)

            for name, info in dupecount.items():
                countwriter.writerow([name, info["count"], info["filesize"], info["hash"]])


    print (dupecount)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Dupe Counter",
                                     description="Given a CSV of file hashes generated by Dupefinder, will count the occurrence of each duplicate.")
    parser.add_argument('dupecsvfile', help="Input CSV file containing dupes")
    parser.add_argument(
        'dupecountfile', help="Output CSV containing the count of each dupe")
    args = parser.parse_args()

    dupecounter(args.dupecsvfile, args.dupecountfile)
