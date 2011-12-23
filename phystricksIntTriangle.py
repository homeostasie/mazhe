from phystricks import *
def IntTriangle():
    pspict,fig = SinglePicture("IntTriangle")

    x=var('x')
    f1=phyFunction(2)
    f2=phyFunction(x)

    surface=SurfaceBetweenFunctions(f1,f2,0,2)
    surface.parameters.color="green"
    surface.f1.parameters.style="solid"
    surface.f1.parameters.color="red"
    surface.f2.parameters=surface.f1.parameters

    pspict.DrawGraphs(surface)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()