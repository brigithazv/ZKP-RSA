package prover

import (
	"RSA verify2/my prime"
	"math"
	"math/rand"
	"time"
)

type Prover struct {
	P           int
	Q           int
	N           int
	Nn          int
	Orla        int
	PublicKey   int
	PrivateKey  int
	A           int
	B           int
	C           int
	S text       int
	D text       int
	ArrivalTime int64
}

func Gen_rand() int {
	return rand.In tn(1000)
}

func Cal(a int, b int) int {
	return a ^ b
}

//10-1000的素数
func (r *Prover) Gen_key() {
	mp := new(my prime.MyPrime)
	mp.Init()
	for {
		num1 := rand.In tn(mp.GetPrimeNum())
		r.P = int(mp.GetPrime(num1))
		for {
			num1 := rand.In tn(mp.GetPrimeNum())
			r.Q = int(mp.GetPrime(num1))
			if r.Q != r.P {
				break
			}
		}
		if r.Q > 10 && r.P > 10 {
			break
		}
	}
	r.N = r.P * r.Q

	r.Orla = (r.P - 1) * (r.Q - 1)
	for {
		num1 := rand.In tn(mp.GetPrimeNum())
		r.PublicKey = int(mp.GetPrime(num1))
		//r.PublicKey = rand.In tn(r.Orla)
		if r.Orla%r.PublicKey != 0 {
			break
		}
	}

	//扩展欧几里得求私钥
	var y int
	my prime.GcdEx(r.PublicKey, r.Orla, &r.PrivateKey, &y)
	if r.PrivateKey < 0 {

		r.PrivateKey = (r.PrivateKey%r.Orla + r.Orla) % r.Orla
	}
}

func (r *Prover) Encrypt(m int) {
	r.S text = my prime.ModPow(m, r.PublicKey, r.N)
}

func (r *Prover) D code(c int) {
	r.D text = my prime.ModPow(c, r.PrivateKey, r.Nn)
}

func Get_currentTime() int64 {
	t1 := time.Now()
	timestamp1 := t1.UnixNano() / 1000
	return timestamp1
}

func Gen_poissonTime(beta float64) float64 {
	x := rand.Float64()
	ln := math.Log(x)
	t := beta * ln
	t = -t
	return t
}

func (this *Prover) Less(other interface{}) bool {
	return this.ArrivalTime < other.(*Prover).ArrivalTime
}

func Delay(t int64) {
	t1 := Get_currentTime()
	for Get_currentTime() < t1+t {

	}
}
