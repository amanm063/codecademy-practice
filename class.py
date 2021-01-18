class Patient:
  def __init__(self, name, age,sex,bmi,num_of_children,smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker

  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex +370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500

    print(self.name + "'s estimated insurance cost is " +str(estimated_cost)+" dollars")
  
  def update_age(self,new_age):
    self.age = new_age
    print(self.name + " is now "+ str(self.age) + " years old.")

  def update_num_of_children(self,new_num_of_children):
    self.num_of_children = new_num_of_children
    print(self.name+ "has "+str(self.num_of_children) + " children.")

  def patient_profile(self):
    patient_profile = {}
    patient_profile["name"] = self.name
    patient_profile["age"] = self.age
    patient_profile["sex"] = self.sex
    patient_profile["bmi"] = self.bmi
    patient_profile["no. of children"] = self.num_of_children
    patient_profile["smoker"] = self.smoker
    return patient_profile


patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker)
print(patient1.estimated_insurance_cost())
print(patient1.update_age(27))
print(patient1.update_num_of_children(3))
print(patient1.patient_profile())
