from cgi import test
import cnn

# Stmts == the number of lines of the code (comments not included)
# Miss == the number of line that have not been reached (for example if an assert function did not get the expected result)
# Cover == the number of lines that have been reached out of the total. 
#     For example: Stmts == 10  }
#                  Miss == 1    } -> cover == 90%
# Missing == the line number that was not reached

nn = cnn.CNN()
nn.model.summary()
nn.model.load_weights('./checkpoint.h5')

# testing for a single NonDementia image
def test1():
  predictions = nn.model.predict(cnn.CNN.predictSetup("./binaryClassificationDataset/test/yes/slice1.png"))
  if(predictions[0][0]>predictions[0][1]):
    test="no"
  elif(predictions[0][1]>predictions[0][0]):
    test="yes"
  assert test != "no", "ERROR: slice1.png from YES is considered NO or the prediction was equal"
  print("Test 1 was successfully passed")
test1()

# testing for a single NonDementia image
def test2():
  predictions = nn.model.predict(cnn.CNN.predictSetup("./binaryClassificationDataset/test/no/slice99.png"))
  if(predictions[0][0]>predictions[0][1]):
    test="no"
  elif(predictions[0][1]>predictions[0][0]):
    test="yes"
  assert test != "yes", "ERROR: slice99.png from NO is considered YES or the prediction was equal"
  print("Test 2 was successfully passed")
test2()

# coverage run -m unittest D:\IP\'binary classification using resnet50'\testing.py
# coverage report -m  D:\IP\'binary classification using resnet50'\testing.py



