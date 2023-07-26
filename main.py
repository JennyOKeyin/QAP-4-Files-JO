# Program Comments.
# Written by: Jennifer Oliver
# Date Written: July 17, 2023 - July 25, 2023
# Description: New insurance policy info for
# One Stop Insurance Company Customers

# Program Imports.
import FormatValues as FV
import time
import datetime
CurrDate = datetime.datetime.now()


# Opens the defaults file and read the values into variable
f = open('OSICDef.dat', 'r')
NEXT_POL_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
DISC_ADD_CAR = float(f.readline())
COST_EXTRA_LI_COV = float(f.readline())
COST_GLASS_COV = float(f.readline())
COST_LOAN_CAR = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())
f.close()


# Program Functions.
def FindLiabilityCost():
    # Determines the amount of liability coverage, if applicable.
    while True:
        OptLiability = input("Do you want extra liability coverage up to $1,000.00 (Y or N): ").upper()
        if OptLiability == "Y":
            OptLiability = COST_EXTRA_LI_COV * NumCars
            break
        elif OptLiability == "N":
            OptLiability = 0.00
            break
        else:
            print("Error - Not a valid option.")

    return OptLiability


def FindGlassCovCost():
    # Determines the amount of glass coverage, if applicable.
    while True:
        OptGlass = input("Do you want optional glass coverage (Y or N): ").upper()
        if OptGlass == "Y":
            OptGlass = COST_GLASS_COV * NumCars
            break
        elif OptGlass == "N":
            OptGlass = 0.00
            break
        else:
            print("Error - Not a valid option.")

    return OptGlass


def FindLoanCost():
    # Determines the amount for loaner car, if applicable.
    while True:
        OptLoanCar = input("Do you want a loaner car (Y or N): ").upper()
        if OptLoanCar == "Y":
            OptLoanCar = COST_LOAN_CAR * NumCars
            break
        elif OptLoanCar == "N":
            OptLoanCar = 0.00
            break
        else:
            print("Error - Not a valid option.")


    return OptLoanCar


def GetPayOption():
    # Determine the amount/schedule based on the pay option chosen.
    PayList = ["Full", "Monthly"]

    while True:
        PayOpt = input("Enter the payment option choice (Full or Monthly): ").title()
        if PayOpt == "":
            print("Error - Payment option cannot be blank.")
        elif PayOpt not in PayList:
            print("Error - Not a valid payment option.")
        else:
            break

    return PayOpt


def ValProv():
    # Validate the province.
    ProvLst = ["NL", "NS", "PE", "QC", "ON", "MB", "SK", "AB", "ON", "BC"]

    while True:
        Prov = input("Enter the Province (LL): ").upper()

        if Prov == "":
            print("Error - Province cannot be blank.")
        elif len(Prov) != 2:
            print("Error - Province must be 2 letters only.")
        elif Prov not in ProvLst:
            print("Error - Not a valid province.")
        else:
            return Prov


def CalculateInsPrem(NumCars):
    # Calculates the insurance premiums based on the above inputs and calculations
    if NumCars <= 1:
        InsPrem = BASIC_PREM
    else:
        InsPrem = ((BASIC_PREM - (DISC_ADD_CAR * BASIC_PREM)) * (NumCars - 1) + BASIC_PREM)

    return InsPrem


def ProgressBar():
    # Provides the user with a progress bar to visualize that the info is saving.
    total = 10
    for i in range(1, total + 1):
        progress = i / total
        bar_length = 20
        filled_length = int(progress * bar_length)
        remaining_length = bar_length - filled_length
        bar = '█' * filled_length + '-' * remaining_length
        percentage = int(progress * 100)
        print(f'\rProgress: [{bar}] {percentage}% ({i}/{total})', end='', flush=True)
        time.sleep(0.5)  # Adjust sleep duration to control the speed of progress


# Main Program.
while True:
    while True:
        CustFirstName = input("Enter the customers first name (END to quit): ").title()
        if CustFirstName.upper() == "END":
            break
        else:
            break
    if CustFirstName.upper() == "END":
        break
    CustLastName = input("Enter the customers last name: ").title()
    FullName = CustFirstName + " " + CustLastName
    StAddress = input("Enter the street address: ").title()
    City = input("Enter city: ").title()
    Prov = ValProv()
    FullAdd = City + "," + " " + Prov

    PostalCode = input("Enter the postal code: ").upper()
    PhoneNum = input("Enter the phone number (999-999-9999): ")
    NumCars = int(input("Enter the number of cars being insured: "))

    OptLiability = FindLiabilityCost()
    OptGlass = FindGlassCovCost()
    OptLoanCar = FindLoanCost()

    InsPrem = CalculateInsPrem(NumCars)
    PayOpt = GetPayOption()
    TotalExCost = OptLiability + OptGlass + OptLoanCar
    TotalInsPrem = InsPrem + TotalExCost
    HST = HST_RATE * TotalInsPrem
    TotalCost = TotalInsPrem + HST

    MonthPay = (PROCESS_FEE + TotalCost) / 8

    PayAmt = PayOpt
    while True:
        if PayOpt == "Monthly":
            PayAmt = MonthPay
            print(PROCESS_FEE)
            break
        elif PayOpt == "Full":
            PayAmt = TotalCost
            break

    InDate = CurrDate.now().date()
    NextPayMonth = datetime.date(CurrDate.year, CurrDate.month + 1, 1)

    # Program Display:
    print()
    print()
    print("                  One Stop Insurance Company")
    print("                       Insurance Policy")
    print("________________________________________________________________")
    print()
    print(f"Policy #: {NEXT_POL_NUM:<4d}                   Date issued:         {InDate}")
    print(f"                                 Next payment Date:   {NextPayMonth}")
    print("________________________________________________________________")
    print()
    print(f"Client Details:                  Policy Details:")
    print()
    print(f"Name:    {FullName:<24s}Number of Cars Insured:      {NumCars:>2d}")
    print(f"Address: {StAddress:<20s}    Extra Liability:     {FV.FDollar2(OptLiability):>10s}")
    print(f"         {FullAdd:<20s}    Glass Coverage:      {FV.FDollar2(OptGlass):>10s}")
    print(f"         {PostalCode:<6s}                  Loaner Car:          {FV.FDollar2(OptLoanCar):>10s}")
    print(f"Phone:   {PhoneNum:<12s}            Total Add-On Cost:   {FV.FDollar2(TotalExCost):>10s}")

    print("________________________________________________________________")
    print()
    print(f"Cost Break Down:                 Payment Plan Details:")
    print()
    print(f"Insurance Premiums:{FV.FDollar2(InsPrem):>10s}    Payment plan option:    {PayOpt:>7s}")
    print(f"Subtotal:          {FV.FDollar2(TotalInsPrem):>10s}    Processing fee:      {FV.FDollar2(PROCESS_FEE) if PayOpt == 'Monthly' else 'N/A':>10s} ")
    print(f"HST:               {FV.FDollar2(HST):>10s} ")
    print(f"Total Policy Cost: {FV.FDollar2(TotalCost):>10s}    {(f'Total Due:           {FV.FDollar2(PayAmt):>10s}' if PayOpt == 'Full' else f'Total monthly payments: {FV.FDollar2(PayAmt):<10s}')}")
    print("________________________________________________________________")
    print()
    print(f"                    Thank you for your business! ")
    print()
    print("Saving policy data ...")

    # Progress bar.
    ProgressBar()
    print()
    print("Policy information processed and saved.")
    print()

    # HouseKeeping.
    # Write the values to a file for future reference.
    f = open("Policies.dat", "a")
    f.write(f"{NEXT_POL_NUM}, ")
    f.write(f"{InDate}, ")
    f.write(f"{CustFirstName}, ")
    f.write(f"{CustLastName}, ")
    f.write(f"{StAddress}, ")
    f.write(f"{City}, ")
    f.write(f"{Prov}, ")
    f.write(f"{PostalCode}, ")
    f.write(f"{PhoneNum}, ")
    f.write(f"{NumCars}, ")
    f.write(f"{('Y' if OptLiability == COST_EXTRA_LI_COV * NumCars else 'N')}, ")
    f.write(f"{('Y' if OptGlass == COST_GLASS_COV * NumCars else 'N')}, ")
    f.write(f"{('Y' if OptLoanCar == COST_LOAN_CAR * NumCars else 'N')}, ")
    f.write(f"{PayOpt}, ")
    f.write(f"{TotalInsPrem}\n")
    f.close()

    # Update any default values based on the processing requirements
    NEXT_POL_NUM += 1
