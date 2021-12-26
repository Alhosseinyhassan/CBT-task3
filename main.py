############################     Mass defect    ######################
isotopes = DataBase.getElement("C").getIsotopeDistribution().getContainer()
carbon_isotope_difference = isotopes[1].getMZ() - isotopes[0].getMZ()
isotopes = DataBase.getElement("N").getIsotopeDistribution().getContainer()
nitrogen_isotope_difference = isotopes[1].getMZ() - isotopes[0].getMZ()

print("Mass difference between 12C and 13C:", carbon_isotope_difference)
print("Mass difference between 14N and N15:", nitrogen_isotope_difference)
print("Relative deviation:", 100 * (carbon_isotope_difference -
                                    nitrogen_isotope_difference) / carbon_isotope_difference, "%")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
helium = ElementDB().getElement("He")
isotopes = helium.getIsotopeDistribution()
mass_sum = 2 * PROTON_MASS_U + 2 * ELECTRON_MASS_U + 2 * NEUTRON_MASS_U
helium4 = isotopes.getContainer()[1].getMZ()
print("Sum of masses of 2 protons, neutrons and electrons:", mass_sum)
print("Mass of He4:", helium4)
print("Difference between the two masses:", 100 * (mass_sum - helium4) / mass_sum, "%")
# Molcular formula
methanol = EmpiricalFormula("CH3OH")
water = EmpiricalFormula("H2O")
ethanol = EmpiricalFormula("CH2") + methanol
print("Ethanol chemical formula:", ethanol.toString())
print("Ethanol composition:", ethanol.getElementalComposition())
print("Ethanol has", ethanol.getElementalComposition()[b"H"], "hydrogen atoms")
# Isotopic Distributions
methanol_isoDist = {"mass": [], "abundance": []}
ethanol_isoDist = {"mass": [], "abundance": []}


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

print("Coarse Isotope Distribution:")
isotopes = ethanol.getIsotopeDistribution(CoarseIsotopePatternGenerator(4))
prob_sum = sum([iso.getIntensity() for iso in isotopes.getContainer()])
print("This covers", prob_sum, "probability")
for iso in isotopes.getContainer():
    print("Isotope", iso.getMZ(), "has abundance", iso.getIntensity() * 100, "%")
    methanol_isoDist["mass"].append(iso.getMZ())
    methanol_isoDist["abundance"].append((iso.getIntensity() * 100))
    
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


print("Fine Isotope Distribution:")
isotopes = ethanol.getIsotopeDistribution(FineIsotopePatternGenerator(1e-3))
prob_sum = sum([iso.getIntensity() for iso in isotopes.getContainer()])
print("This covers", prob_sum, "probability")
for iso in isotopes.getContainer():
    print("Isotope", iso.getMZ(), "has abundance", iso.getIntensity() * 100, "%")
    ethanol_isoDist["mass"].append(iso.getMZ())
    ethanol_isoDist["abundance"].append((iso.getIntensity() * 100))
    
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


plt.figure(figsize=(10, 7))
plt.subplot(1, 2, 1)
plt.title("Isotopic distribution of methanol")
plotDistribution(methanol_isoDist)
plt.xlabel("Atomic mass (u)")
plt.ylabel("Relative abundance (%)")

plt.subplot(1, 2, 2)
plt.title("Isotopic distribution of ethanol")
plotDistribution(ethanol_isoDist)
plt.xlabel("Atomic mass (u)")
plt.ylabel("Relative abundance (%)")

plt.savefig("methanol_ethanol_isoDistribution.png")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

print("Fine Isotope Distribution:")
isotopes = ethanol.getIsotopeDistribution(FineIsotopePatternGenerator(1e-6))
prob_sum = sum([iso.getIntensity() for iso in isotopes.getContainer()])
print("This covers", prob_sum, "probability")
for iso in isotopes.getContainer():
    print("Isotope", iso.getMZ(), "has abundance", iso.getIntensity() * 100, "%")
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

isotopes = ethanol.getIsotopeDistribution(CoarseIsotopePatternGenerator(5, True))
for iso in isotopes.getContainer():
    print("Isotope", iso.getMZ(), "has abundance", iso.getIntensity() * 100, "%")
