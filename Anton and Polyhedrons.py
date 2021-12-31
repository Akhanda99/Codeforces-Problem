polyhedrons={"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
n=int(input())
face=0
for i in range(0,n):
    inp=input()
    face+=polyhedrons[inp]
print(face)