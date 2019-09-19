from math import sqrt

class vec3:

    def __init__(self, vec=None, in_list=None, x=None, y=None, z=None):
        if vec is not None:
            self.e = [vec[0], vec[1], vec[2]]
            return
        elif in_list is not None:
            self.e = in_list
            return
        self.e = [x, y, z]

    def __getitem__(self, index):
        return self.e[index]

    @property
    def x(self):
        return self.e[0]
    @property
    def y(self):
        return self.e[1]
    @property
    def z(self):
        return self.e[2]

    def __eq__(self, vec):
        return ((vec[0]==self.e[0]) and (vec[1]==self.e[1]) and (vec[2]==self.e[2]))

    # operators that take vecs
    # in place
    def __iadd__(self, vec):
        self.e[0] = (self.e[0]+vec[0])
        self.e[1] = (self.e[1]+vec[1])
        self.e[2] = (self.e[2]+vec[2])
        return self

    def __isub__(self, vec):
        self.e[0] -= vec[0]
        self.e[1] -= vec[1]
        self.e[2] -= vec[2]
        return self

    def __imul__(self, vec):
        self.e[0] *= vec[0]
        self.e[1] *= vec[1]
        self.e[2] *= vec[2]
        return self

    def __truediv__(self, vec):
        self.e[0] /= vec[0]
        self.e[1] /= vec[1]
        self.e[2] /= vec[2]
        """
        self.e[0] = self.e[0]/vec[0]
        self.e[1] = self.e[1]/vec[1]
        self.e[2] = self.e[2]/vec[2]
        """
        return self

    # operators that take vecs
    # construct a new vec3
    def __add__(self, vec):
        return vec3(x=(vec[0]+self.e[0]), y=(vec[1]+self.e[1]), z=(vec[2]+self.e[2]))

    def __sub__(self, vec):
        return vec3(x=self.e[0]-vec[0],  y=self.e[1]-vec[1],  z=self.e[2]-vec[2])

    def __div__(self, vec):
        return vec3(x=self.e[0]/vec[0],  y=self.e[1]/vec[1],  z=self.e[2]/vec[2])

    def __mul__(self, vec):
        return vec3(x=self.e[0]*vec[0],  y=self.e[1]*vec[1],  z=self.e[2]*vec[2])

    # in place add float method
    
    def iadd_float(self, in_float):
        self.e[0] += in_float
        self.e[1] += in_float
        self.e[2] += in_float

    def isub_float(self, in_float):
        self.e[0] -= in_float
        self.e[1] -= in_float
        self.e[2] -= in_float

    def imul_float(self, in_float):
        self.e[0] *= in_float
        self.e[1] *= in_float
        self.e[2] *= in_float

    def idiv_float(self, in_float):
        self.e[0] /= in_float
        self.e[1] /= in_float
        self.e[2] /= in_float

    def length(self):
        return sqrt(self.e[0]*self.e[0] + self.e[1]*self.e[1] + self.e[2]*self.e[2])

    def scale_to(self, in_float):
        self.idiv_float( self.length() )
        self.imul_float( in_float )

    #TODO add imul, idiv, isub iadd for float nums

# constructs a new vector in the addition
def add_float(vec, in_float): 
    return vec3(x=(vec[0]+in_float), y=(vec[1]+in_float), z=(vec[2]+in_float))

def sub_float(vec, in_float): 
    return vec3(x=(vec[0]-in_float), y=(vec[1]-in_float), z=(vec[2]-in_float)) 

def mul_float(vec, in_float): 
    return vec3(x=(vec[0]*in_float), y=(vec[1]*in_float), z=(vec[2]*in_float))

def div_float(vec, in_float): 
    return vec3(x=(vec[0]/in_float), y=(vec[1]/in_float), z=(vec[2]/in_float))


def dot(vec1, vec2):
    return (vec1[0]*vec2[0] + vec1[1]*vec2[1] + vec1[2]*vec2[2])

def lerp(start_vec, end_vec, percent):

    result = vec3(end_vec-start_vec)
    result.imul_float(percent)
    result += start_vec
    return result

def unit_vector(vec):
    return div_float(vec, vec.length())
"""
public:
	float e[3];
	vec3() {}
	vec3(const vec3& vecIn);
	vec3(float e0, float e1, float e2) {
		e[0] = e0;
		e[1] = e1;
		e[2] = e2;
	}

	inline float x() const { return e[0]; }
	inline float y() const { return e[1]; }
	inline float z() const { return e[2]; }
	inline float r() const { return e[0]; }
	inline float g() const { return e[1]; }
	inline float b() const { return e[2]; }

	///+ left hand opperator gets the positive version
	inline const vec3& operator+() const { return *this; }
	inline vec3 operator-() const { return vec3(-e[0], -e[1], -e[2]); }
	inline float operator[](const int i) const { return e[i]; }
	inline float& operator[](const int i) { return e[i]; }

	inline vec3& operator+=(const vec3& v2);
	inline vec3& operator-=(const vec3& v2);
	inline vec3& operator*=(const vec3& v2);
	inline vec3& operator/=(const vec3& v2);

	inline vec3& operator*=(const float t);
	inline vec3& operator/=(const float t);
	inline vec3& operator-=(const float t);
	inline vec3& operator+=(const float t);

	inline float length() {
		//return sqrt(e[0] * e[0] + e[1] * e[1] + e[2] * e[2]);
		return sqrt(squared_length());
	}
	inline float squared_length() {
		return (e[0] * e[0] + e[1] * e[1] + e[2] * e[2]);
	}

	void make_unit_vector();

	inline void scale_to(const float len);
};
"""