import time

class PID:
    def __init__(self, P, I, D,SP):
        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.SetPoint = SP
        self.current_time = time.time()
        self.prev_error = 0.0
        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0
        self.prev_time = self.current_time
        self.u = 0
        self.direct = 1
    def update(self,feedback_value):
    
        #time differance
        self.current_time = time.time()
        delta_time = (self.current_time - self.prev_time)*10000
        #print(delta_time)
        self.prev_time = self.current_time
        
        #propotional
        error = self.SetPoint - feedback_value
        self.PTerm = error
        
        #integral
        self.ITerm = self.ITerm + error*delta_time

        #derivative
        delta_error = error - self.prev_error
        dedt = delta_error / delta_time
        self.DTerm =dedt

        # control signal 
        U = (self.Kp * self.PTerm) + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)
        pwm = abs(U)
        if pwm > 100:
            pwm =100
        self.u = pwm
        if U<0 :
            self.direct = -1
    
    def getSignal(self):
        return self.u
    
    def getdirect(self):
        return self.direct

    def getSP(self):
        return self.SetPoint
    
    def getPTerm(self):
        return self.PTerm
    
    def getITerm(self):
        return self.ITerm
    
    def getDTerm(self):
        return self.DTerm