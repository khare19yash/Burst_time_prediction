def affine_forward(x,w,b):
    
    out = np.dot(x,w) + b
    cache = (x,w,b)
    return out,cache

def affine_backward(dout,cache):
    
    x,w,b = cache
    dx = np.dot(dout,w.T) 
    dw = np.dot(x.T,dout)
    db = np.sum(dout,axis=0)
    return dx,dw,db

def relu_forward(x):
    
    out = np.max(x,0)
    cache = x
    return out,cache

def relu_backward(dout,cache):
    
    dx = dout
    dx[x<=0] = 0
    return dx

def rnn_step_forward(x,h0):
    
    h_next = np.dot(x,Wxh) + np.dot(h0,Whh) + b
    
    
   
    