def link2id():
    link = input("link: ")
    ids = link.split("#")[1:]
    ids.sort()
    print(ids)


def id2link(ids):
    ids.sort()
    link = "https://ssimeonoff.github.io/cards-list#"
    print(link + "#".join(ids))


# CardSect
GainProduction = ["040", "051", "099", "137", "175", "230", "236"]
PlayGainMC = [
    "007",
    "031",
    "107",
    "109",
    "251",
    "C27",
    "T04",
    "T06",
    "X08",
    "X25",
    "X30",
]
PayMCLess = ["020", "070", "079", "094", "105", "150", "258", "C36", "C49", "X18"]
GainCard = ["006", "014", "073", "090", "110", "185", "199", "208", "C41", "X29"]
GainVP = [
    "012",
    "019",
    "026",
    "074",
    "081",
    "092",
    "096",
    "128",
    "131",
    "143",
    "163",
    "197",
    "249",
    "259",
    "260",
    "X35",
]
GreenCard = ["047", "055", "059", "060", "T15"]
VPCard = [
    "013",
    "021",
    "025",
    "044",
    "046",
    "057",
    "082",
    "084",
    "091",
    "114",
    "116",
    "119",
    "135",
    "139",
    "166",
    "168",
    "176",
]
Colonies = ["CERES", "LUNA", "PLUTO", "TRITON"]
NotUse = ["018", "028", "042", "048", "049", "058", "095", "129", "174", "C43"]

CardSect = (
    GainProduction + PlayGainMC + PayMCLess + GainCard + GainVP + GreenCard + VPCard
)
CardSect.sort()


# TerraformSect
TGreenCard = ["042", "055", "059", "087", "142", "162", "193", "P10", "T15"]
TNotUse = [
    "018",
    "043",
    "048",
    "058",
    "068",
    "106",
    "122",
    "126",
    "146",
    "164",
    "174",
    "202",
    "203",
    "T01",
    "T13",
]


def main():
    # link2id()

    # id2link(GainProduction)
    # id2link(PlayGainMC)
    # id2link(PayMCLess)
    # id2link(GainCard)
    # id2link(GainVP)
    # id2link(GreenCard)
    # id2link(VPCard)
    # id2link(CardSect)
    # print(len(CardSect))
    # id2link(Colonies)
    # id2link(NotUse)

    id2link(TGreenCard)
    id2link(TNotUse)


if __name__ == "__main__":
    main()
10 + 4 * 6
34
