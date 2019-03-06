class Dictionary:
    def sort_dict(self):
        try:
            import operator
            d = {1: 10, 0: 9, 3: 6, 2: 7, 4: 11}
            print("original dictionary is : ", d)
            sort_d = sorted(d.items(), key=operator.itemgetter(0))
            print("sorting in ascending order : ", sort_d)
            sort_d = sorted(d.items(), key=operator.itemgetter(0), reverse=True)
            print("sorting in reverse order : ", sort_d)
        except Exception as e:
            print(e)


d_obj = Dictionary()
d_obj.sort_dict()
