#import operator
#data set => already taken for prediction
dataset = {
"Ans":             ["Yes","No","Yes","Yes","No","Yes","Yes","No","Yes","No","No","Yes"],
"Alternate":       ["Yes","Yes","No","No","No","Yes","No","No","Yes","Yes","No","Yes"],
"Bar":             ["No","Yes","Yes","Yes","No","No","Yes","No","No","Yes","Yes","No"],
"Fri/Sat":         ["Yes","No","No","No","Yes","No","Yes","Yes","Yes","No","No","Yes"],
"Hungry":          ["No","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes"],
"Patrons":         ["Some","Full","Full","None","Full","Some","Some","Full","Full","Some","Full","Some"],
"Price":           ["High","Low","Low","Low","High","High","High","Low","High","Low","High","Low"],
"Raining":         ["Yes","Yes","No","No","No","No","No","Yes","No","Yes","No","No"],
"Reservation":     ["Yes","Yes","No","Yes","No","No","Yes","No","Yes","No","Yes","Yes"],
"Type":            ["French","Thai","Burger","Italian","Italian","Thai","French","Thai","Burger","Italian","Burger","French"],
"WaitEstimate":    ["10-30","0-10",">60","30-60","10-30","0-10",">60","30-60","30-60",">60","10-30","0-10"]
}

#input data to test or predict
test_case={
"Alternate":      "Yes",
"Bar":            "No",
"Fri/Sat":        "No",
"Hungry":         "Yes",
"Patrons":        "Full",
"Price":          "High",
"Raining":        "No",
"Reservation":    "No",
"Type":           "Thai",
"WaitEstimate":   "10-30"
}

def build_probs(ds, test_case):
    ans = ds["Ans"]#output attribute (ans)
    length = len(ans) #total length of output(ans)
    ans_set = set(ans) #unique (individual) classes yes and no
    count_ans = {k: ans.count(k) for k in ans_set}
    calc_prob = {k: count_ans[k] / length for k in ans_set}
    for ft in ds:
        if ft != "Ans":
            counts = {attr: {k: 0 for k in ans_set} for attr in set(ds[ft])}
            for i in range(length):
                counts[ds[ft][i]][ans[i]] +=1
            for k in ans_set:
                calc_prob[k] *= counts[test_case[ft]][k]/ count_ans[k]
    print(test_case,":\n",max(calc_prob, key=calc_prob.get))

build_probs(dataset, test_case)
