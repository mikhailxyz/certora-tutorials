(declare-const p Bool)
(declare-const q Bool)

(define-fun equality() Bool
   (= (=> p q) 
   (= (and p q) p)
))

; by asserting that equality is false, we are asserting that there are no
; P and Q values for which the two expressions are unequal (and thus the expression is VALID)
; if we assert that equality is true, we are asserting that there are P and Q values for which
; the expression is true (and thus the expression is SATISFIABLE) but there are no
; guarantees that the expression is VALID
(assert (not equality))
(check-sat)