# -*- coding: utf8 -*-
from phystricks import *
def NOCGooYRHLCn():
	pspict,fig = SinglePicture("NOCGooYRHLCn")
	mx = -0.5
	Mx = 7
	x0 = 5
	dx = 1
	x=var('x')
	f = phyFunction(-((x+0.5)/3)**2+4+x).graph(mx,Mx)
	f.parameters.color="brown"

	P=f.get_point(x0)
	P.put_mark(0.4,P.advised_mark_angle(pspict),"$f(x)$",pspict=pspict)
	Px=Point(P.x,0)
	Px.put_mark(0.2,-90,"$x$",pspict=pspict,position="N")

	Q=Point(P.x+dx,0)
	Q.put_mark(0.2,-90,"$x+\Delta x$",pspict=pspict,position="N")

	surface=SurfaceUnderFunction(f,0,x0)
	surface.parameters.hatched()
	surface.parameters.hatch.color="blue"
	rectangle=Rectangle(P,Q)
	rectangle.parameters.hatched()
	rectangle.parameters.hatch.color="red"
	rectangle.parameters.color="red"
	rectangle.parameters.style="dashed"
	

	pspict.DrawGraphs(surface,f,rectangle,P,Px,Q)
	pspict.axes.no_graduation()
	pspict.DrawDefaultAxes()
	pspict.dilatation(1)
	fig.conclude()
	fig.write_the_file()
