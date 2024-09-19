import matplotlib.pyplot as plt

dt = 0.01
m = 1
k = 1
x0 = 0.1
v0 = 0.1


def force_function(k,x):
    return(-k*x)

def explicit(x,v, dt,k,m,f):
    x_new = x+v*dt
    v_new = v + (f/m)*dt
    return(x_new, v_new)

def symplictic(x,v,dt,k,m,f):  
    v_new = v+ (f/m)*dt
    x_new = x+ v_new*dt
    return(x_new, v_new)

x_e = [x0]
v_e = [v0]
f0= (force_function(k,x_e[0]))
f_e = [f0]
t_e = [dt]

for i in range(10000):
    xl, vl = explicit(x_e[i], v_e[i], dt, k, m, f_e[i])
    x_e.append(xl)
    v_e.append(vl)
    f_e.append(force_function(k,xl))
    t_e.append(t_e[i]+dt)

x_s = [x0]
v_s = [v0]
f_s = [f0]
t_s = [dt]

for i in range(10000):
    xl,vl = symplictic(x_s[i], v_s[i], dt,k,m,f_s[i])
    x_s.append(xl)
    v_s.append(vl)
    f_s.append(force_function(k,xl))
    t_s.append(t_s[i]+dt)

plt.figure()
plt.plot(t_e, x_e, label = "explicit")
plt.plot(t_s,x_s, label ="Symplectic")
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.legend()
plt.show()


