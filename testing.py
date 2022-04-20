from cgi import test
import nn

# Stmts == the number of lines of the code (comments not included)
# Miss == the number of line that have not been reached (for example if an assert function did not get the expected result)
# Cover == the number of lines that have been reached out of the total. 
#     For example: Stmts == 10  }
#                  Miss == 1    } -> cover == 90%
# Missing == the line number that was not reached

nn = nn.NN()
nn.model.summary()
nn.load_model_weights('./alzheimer_model.h5');

# testing for a single NonDementia image
def test1():
  test = nn.predict('./Cognitively_normal/0.png');
  assert test != "Dementia", "ERROR: 0.png from Cognitively_normal should have been declared as NonDementia"
  print("Test 1 was successfully passed");
test1()

# testing for a single Dementia image
def test2():
  test = nn.predict('./AD_Dementia/0.png');
  assert test != "NonDementia", "ERROR: 0.png from AD_Dementia should have been declared as Dementia"
  print("Test 2 was successfully passed");
test2()

#testing the first 40 NonDementia images
def test3():
  for x in range(0, 40):
    path = f"./Cognitively_normal/{x}.png"
    test = nn.predict(path);
    assert test != "Dementia", f"ERROR: {x}.png from Cognitively_normal should have been declared as NonDementia"
    print(f"Test {x+3} was successfully passed");
test3()

#testing the first 40 Dementia images
def test4():
  for x in range(0, 40):
    path = f"./AD_Dementia/{x}.png"
    test = nn.predict(path);
    assert test != "NonDementia", f"ERROR: {x}.png from AD_Dementia should have been declared as Dementia"
    print(f"Test {x+43} was successfully passed");
test4()