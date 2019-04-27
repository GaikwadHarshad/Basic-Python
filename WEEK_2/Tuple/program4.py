"""  Write a Python program to create the clone of a tuple.  """

from myprograms.Utility import UtilityDS


class CreateClone:
    def clone(self):
        try:
            # original tuple
            tuple1 = ('A', 'B', 'C', 'D', 'E', 'F', 'G', [])
            print("Original tuple : ", tuple1)
            # function call for cloning tuple
            new_tuple = UtilityDS.clone_tuple(tuple1)
            print("Clone tuple : ", new_tuple)
            # append data in cloned tuple
            new_tuple[7].append("harsh")
            print("Append clone tuple : ", new_tuple)
        except Exception as e:
            print(e)


CreateClone_object = CreateClone()
CreateClone_object.clone()
