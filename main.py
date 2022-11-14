# Stuff to do:

# TODO figure out a way to quantify accuracy
# TODO make a function that takes in new images & re-trains model so this code can be re-used every year
# FIXME duplicate name problem?? what if future people have same names
# TODO make some form of UI (chrome extension?)

import knn

pred1 = knn.predict("./data/test/naina-horning-1.jpeg", model_path="./model/knn")
pred2 = knn.predict("./data/test/yue-cao-1.png", model_path="./model/knn")
pred3 = knn.predict("./data/test/rex-barnes-1.jpeg", model_path="./model/knn")

print(pred1) # wrong -> predicts "Shin Yeong Park" instead of someone else
print(pred2) # correct
print(pred3) # wrong -> predicts "unknown" instead of "Rex Barnes"
# FIXME ACCURACY ISSUES