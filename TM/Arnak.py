# def link2id():
#     link = input("link: ")
#     ids = link.split("#")[1:]
#     ids.sort()
#     print(ids)


# def id2link(ids):
#     link = "https://ssimeonoff.github.io/cards-list#"
#     print(link + "#".join(ids))


# PlayGainMC = ["031", "107", "109", "251", "C27", "T04", "T06", "X25", "X30"]
# PayMCLess = ["020", "070", "079", "094", "105", "150", "C36", "C49", "X18"]

ALL = """Car
  - Boat
  - Upgrade""".split(
    "\n  - "
)
ALL.sort()


def main():
    print(ALL)


if __name__ == "__main__":
    main()
