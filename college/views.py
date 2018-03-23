
from django.http import HttpResponse
from django.shortcuts import render


def collegeCode(request):
    # return "abc"
    # return HttpResponse("success")
    return render(request,"code.html")

def genCode(request):
    date = request.POST.get("date", "")
    name = request.POST.get("name", "")
    college = request.POST.get("college", "")
    project = request.POST.get("project", "")
    quantity = request.POST.get("quantity", "")

    copyname = name
    name = name.split()
    if len(name) > 1:
        name = name[1]
    else:
        name = ""
    # Code: CollegeCode + ProjectCode + LastName + Date(MMDDYYYY)
    code = college + project + name + date.replace('/', '')

    # set price
    if project == 'P':
        price = 40
        pname = "Pink Answer Sheets"
    else:
        price = 35
        pname = "Blue Answer Sheets"

    amount = int(quantity) * price

    with open("output.txt", "w") as f:
        f.write("Date: " + date + "\n")
        f.write("Name: " + copyname+ "\n")
        if college == "1":
            college = "University of Houston"
        elif college == "2":
            college = "University of Houston Downtown"
        else:
            college = "University of Houston SugarLand"

        f.write("College: " + college + "\n")
        f.write("Project: " + pname+ "\n")
        f.write("Unique Code: " + code+ "\n")
        f.write("Amount: " + str(amount) +"$")

    return HttpResponse("Output.txt file is generated, please check the corresponding folder............Go Back to Try again....... Designed by Harshitha Krishna Thallaparthi.")