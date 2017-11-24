
# les modules a importer doivent etre integes au path python
import sys
sys.path.append("/path")

import exemple9_fonction_moyenne as prefix

moyenne1 = prefix.moyenne( [3,8,9])
moyenne2 = prefix.moyenne( list(range(100)) )

import exemple9_fonction_moyenne
moyenne1 = exemple9_fonction_moyenne.moyenne( [3,8,9])
moyenne2 = exemple9_fonction_moyenne.moyenne( list(range(100)) )

print("liste : ", [3,8,9] , "moyenne :", moyenne1)
print("liste : ", list(range(100)) , "moyenne :", moyenne2)