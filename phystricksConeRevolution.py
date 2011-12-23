from phystricks import *
def ConeRevolution():
    pspict,fig = SinglePicture("ConeRevolution")

    h=3
    R=2
    x=var('x')
    f=phyFunction((SR(h)/R)*x).graph(0,R)

    pspict.axes.single_axeX.axes_unit=AxesUnit(R,"R")
    pspict.axes.single_axeY.axes_unit=AxesUnit(h,"h")

    P=Point(R,h)
    P.put_mark(0.1,45,"$(R,h)$",automatic_place=pspict)

    angle = Angle(Point(1,0),Point(0,0),P,r=0.7)
    angle.parameters.color="red"
    angle.put_mark(0.3,angle.advised_mark_angle,"$\\alpha$")

    pspict.DrawGraphs(f,P,angle)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()