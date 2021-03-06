import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th
import Rhino.Geometry.Intersect as int
import ghpythonlib.components as gc
matpts_a=[[None for i in range(1)]for j in range(len(lines))]
for i in range(len(matpts_a)):
    matpts_a[i].pop(0)
for i in range(len(lines)):
    matpts_a[i]=rs.DivideCurve(lines[i],5)
matlines_a=[[None for i in range(1)]for j in range(len(lines))]
for i in range(len(matlines_a)):
    matlines_a[i].pop(0)
#a=matpts_a[0]
cent_a=rs.DivideCurve(crvA,50)
pt_sum_a = (cent_a[0])
for i in range(1, len(cent_a)):
    pt_sum_a += (cent_a[i])
cent_a= pt_sum_a / len(cent_a)
cent_b=rs.DivideCurve(crvB,50)
pt_sum_b = (cent_b[0])
for i in range(1, len(cent_b)):
    pt_sum_b += (cent_b[i])
cent_b= pt_sum_b / len(cent_b)
#a=cent_b
for i in range(len(lines)):
    for j in range(len(matpts_a[0])):
        matlines_a[i].append(rg.Line(cent_a,matpts_a[i][j]))
#a=matlines_a[0]
#print len(matpts_a[2])
matpts_aa=[[[None for i in range(2)]for j in range(len(matlines_a[0]))]for k in range(len(lines))]
#for i in range(len(matpts_aa)):
#    matpts_aa[i].pop(0)
matpts_ll=[[[None for i in range(2)]for j in range(len(matlines_a[0]))]for k in range(len(lines))]
Lines_A=[[None for i in range(1)]for j in range(len(lines))]
for k in range(2):
    for i in range(len(lines)):
        for j in range(len(matlines_a[0])):
#        for k in range(2):
            matpts_aa[i][j].pop(0)
            matpts_ll[i][j].pop(0)
#            matpts_aa[i][j].pop(1)
for i in range(len(Lines_A)):
    Lines_A[i].pop(0)

for i in range(len(lines)):
    for j in range(len(matlines_a[i])):
        ccx=(int.Intersection.CurveLine(crvA,matlines_a[i][j],0.2,0.2))
        for xe in ccx:
            matpts_aa[i][j].append(xe.PointA)
print matpts_ll
for i in range(len(lines)):
    for j in range(len(matlines_a[0])):
#        for k in range(2):
        matpts_ll[i][j].append(rg.Line(cent_a,matpts_aa[i][j][0]))
        matpts_ll[i][j].append(rg.Line(cent_a,matpts_aa[i][j][1]))

for i in range(len(lines)):
    for j in range(len(matlines_a[0])):
       for k in range(2):
#            if (gc.UnitVector(rs.VectorCreate(matpts_ll[i][j][k].From,matpts_ll[i][j][k].To)) - gc.UnitVector(rs.VectorCreate(matlines_a[i][j].From,matlines_a[i][j].To))) :
            if abs(sum(gc.UnitVector(rs.VectorCreate(matlines_a[i][j].From,matlines_a[i][j].To)))-sum(gc.UnitVector(rs.VectorCreate(matpts_ll[i][j][k].From,matpts_ll[i][j][k].To))))<0.002:
#                print i,j,k
                Lines_A[i].append(matpts_ll[i][j][k])

####################
data_ratio=[[None for i in range(1)]for j in range(len(lines))]
for i in range(len(data_ratio)):
    data_ratio[i].pop(0)
for i in range(len(lines)):
    for j in range(len(matlines_a[0])):
        data_ratio[i].append((matlines_a[i][j].Length)/(Lines_A[i][j].Length))

lines_b=[[None for i in range(1)]for j in range(len(lines))]
matpts_bb=[[[None for i in range(2)]for j in range(len(matlines_a[0]))]for k in range(len(lines))]
matpts_b_ll=[[[None for i in range(2)]for j in range(len(matlines_a[0]))]for k in range(len(lines))]
Lines_B=[[None for i in range(1)]for j in range(len(lines))]
for k in range(2):
    for i in range(len(lines)):
        for j in range(len(matlines_a[0])):
#        for k in range(2):
            matpts_b_ll[i][j].pop(0)
            matpts_bb[i][j].pop(0)
for i in range(len(Lines_B)):
    Lines_B[i].pop(0)
#
for i in range(len(lines_b)):
    lines_b[i].pop(0)
for i in range(len(lines)):
    for j in range(len(matlines_a[0])):
#        matpts_b[i].append(rg.Line(cent_b,matlines_a[i][j].Direction))
        ccx=(int.Intersection.CurveLine(crvB,rg.Line(cent_b,matlines_a[i][j].Direction),0.2,0.2))
        for xe in ccx:
            matpts_bb[i][j].append(xe.PointA)
#
for i in range(len(lines)):
    for j in range(len(matlines_a[0])):
##        for k in range(2):
        matpts_b_ll[i][j].append(rg.Line(cent_b,matpts_bb[i][j][0]))
        matpts_b_ll[i][j].append(rg.Line(cent_b,matpts_bb[i][j][1]))

#
for i in range(len(lines)):
    for j in range(len(matlines_a[0])):
       for k in range(2):
            if abs(sum(gc.UnitVector(rs.VectorCreate(matlines_a[i][j].From,matlines_a[i][j].To)))-sum(gc.UnitVector(rs.VectorCreate(matpts_b_ll[i][j][k].From,matpts_b_ll[i][j][k].To))))<0.002:
#                print i,j,k
                Lines_B[i].append(matpts_b_ll[i][j][k])
a=th.list_to_tree(Lines_B)
b=th.list_to_tree(Lines_A)

points=[[None for i in range(1)]for j in range(len(lines))]
Lines_b_f=[[None for i in range(1)]for j in range(len(lines))]
output=[[None for i in range(1)]for j in range(len(lines))]
for i in range(len(Lines_B)):
    Lines_b_f[i].pop(0)
for i in range(len(output)):
    output[i].pop(0)
for i in range(len(points)):
    points[i].pop(0)
e=cent_b
Lines_b_ff=0
#a=th.list_to_tree(Lines_B)
for i in range(len(lines)):
    for j in range(len(matlines_a[0])):
        Lines_b_f[i].append(rg.Line(cent_b,rs.VectorCreate(Lines_B[i][j].From,Lines_B[i][j].To) ,(-(Lines_B[i][j].Length)*data_ratio[i][j])))
        Lines_b_ff=(rg.Line(cent_b,rs.VectorCreate(Lines_B[i][j].From,Lines_B[i][j].To) ,(-(Lines_B[i][j].Length)*data_ratio[i][j])))
        points[i].append(Lines_b_ff.To)
#        print (Lines_B[i][j].Length)*data_ratio[i][j]
#       for k in range(2):
c=th.list_to_tree(Lines_b_f)
d=th.list_to_tree(data_ratio)
for i in range(len(lines)):
    for j in range(len(matlines_a[0])):
        output[i].append(rg.PolylineCurve(points[i]))
output=th.list_to_tree(output)