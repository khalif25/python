def main() :
    triangles_number=int(input("how many Numbers Triangles You want ?"))
    for j in range (1,triangles_number+1):
        for i in range (1,j+1):
            print(i,end=' ')
        print()
    main()
main()
