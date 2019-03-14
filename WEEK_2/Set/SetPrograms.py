# programs to perform operation on set

from myprograms.Utility import UtilityDS


class SetProgram:
    choice = 0

    def display_program(self):
        print("---------------------------------")
        print("1.program to create a set ""\n""2.program to iteration over sets ")
        print("3.program to add member(s) in a set ""\n""4.program to remove item(s) from set ")
        print("5.program to remove an item from a set if it is present in the set")
        print("6.program to create an intersection of sets ""\n""7.program to create a union of sets")
        print("8.program to create set difference""\n""9.program to create a symmetric difference")
        print("10.program to clear a set""\n""11.program to use of frozensets")
        print("12.program to find maximum and the minimum value in a set")
        print("13.Exit""\n")
        while True:
            try:
                print("-------------------------------------------------------")
                self.choice = int(input("Enter your choice to execute program : "))
                ch = UtilityDS.validate_num(self.choice)
                if ch:
                    if self.choice == 1:
                        create = UtilityDS.create_set()
                        print("Set is created: ", create)
                    elif self.choice == 2:
                        print("Set is : ", UtilityDS.create_set())
                        UtilityDS.iteration(UtilityDS.create_set())
                    elif self.choice == 3:
                        city_set = set(["Mumbai"])
                        print("original Set : ", city_set)
                        add_mem = UtilityDS.add_member(city_set)
                        print("After adding members : ", add_mem)

                    elif self.choice == 4:
                        pop_set = UtilityDS.create_set()
                        print("Set : ", pop_set)
                        rem = UtilityDS.remove_item(pop_set)
                        print("Removed some items : ", rem)

                    elif self.choice == 5:
                            rm_set = UtilityDS.create_set()
                            print("Set : ", rm_set)
                            item = int(input("Which item you want to remove : "))
                            i = UtilityDS.validate_num(item)
                            if i:
                                remove = UtilityDS.rem_spec_item(rm_set, item)
                                print("Set : ", remove)
                    elif self.choice == 6:
                        a_set = UtilityDS.create_set()
                        b_set = UtilityDS.create_set2()
                        print("set 1 : ", a_set)
                        print("set 2 : ", b_set)
                        intersect = UtilityDS.intersect(a_set, b_set)
                        print("Intersection of set : ", intersect)

                    elif self.choice == 7:
                        c_set = UtilityDS.create_set()
                        d_set = UtilityDS.create_set2()
                        print("set 1 : ", c_set)
                        print("set 2 : ", d_set)
                        union = UtilityDS.union(c_set, d_set)
                        print("Union of set : ", union)

                    elif self.choice == 8:
                        e_set = UtilityDS.create_set()
                        f_set = UtilityDS.create_set2()
                        print("Set 1: ", e_set)
                        print("Set 2: ", f_set)
                        diff = UtilityDS.difference(e_set, f_set)
                        print("Set Difference : ", diff)

                    elif self.choice == 9:
                        g_set = UtilityDS.create_set()
                        h_set = UtilityDS.create_set2()
                        print("Set 1 : ", g_set)
                        print("Set 2 : ", h_set)
                        sym_diff = UtilityDS.symmetric_diff(g_set, h_set)
                        print("Symmetric difference : ", sym_diff)

                    elif self.choice == 10:
                        i_set = UtilityDS.create_set()
                        print("Set : ", i_set)
                        print("1.View set""\n""2.clear""\n""3.Exit")
                        while 1:
                            ch = int(input("select option : "))
                            c = UtilityDS.validate_num(ch)
                            if c:
                                if ch == 1:
                                    print("Set : ", i_set)
                                elif ch == 2:
                                    clear = UtilityDS.clear_set(i_set)
                                    print("Set is clear :", clear)
                                elif ch == 3:
                                    break
                            else:
                                print("Enter only numbers")

                    elif self.choice == 11:
                        frozen_set = UtilityDS.create_set()
                        print("set is : ", frozen_set)
                        frozen = UtilityDS.fro_set(frozen_set)
                        print("Frozenset object using set : ", frozen)

                    elif self.choice == 12:
                        j_set = UtilityDS.create_set2()
                        print("Set : ", j_set)
                        min1 = UtilityDS.min_set(j_set)
                        print("Minimum : ", min1)
                        max1 = UtilityDS.max_set(j_set)
                        print("Maximum : ", max1)

                    elif self.choice == 13:
                        print("Exiting program........")
                        exit()
                    else:
                        print("You have entered wrong choice ")
                else:
                    print("Invalid choice entered")
            except Exception as e:
                print(e)


SetProgram_object = SetProgram()
SetProgram_object.display_program()
