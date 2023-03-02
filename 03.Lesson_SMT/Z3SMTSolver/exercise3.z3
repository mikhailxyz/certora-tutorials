; 1 - D

(declare-const p Bool)
(declare-const q Bool)
(assert (not (=> p q)))
(push)
(assert (and (not p) (not q)))
(check-sat)
(pop)
(push) 
(assert (and p q))
(check-sat)
(pop)
(push) 
(assert (and (not p) q))
(check-sat)

; 2 - C
(declare-const p Bool)
(declare-const q Bool)

(define-fun impl() Bool
    (=> (or p q) p)
)
(push)
(assert (not impl))
(check-sat)
(get-model)
(pop)
(assert impl)
(check-sat)
(get-model)

; 3 - B

(declare-const p Bool)
(declare-const q Bool)

(define-fun exp() Bool
    (and (and p (or q (not p))) (not q))
)
(push)
(assert (not exp))
(check-sat)
(get-model)
(pop)
(assert exp)
(check-sat)
(get-model)

; 4 - A

(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)

(define-fun exp() Bool
    (= (not (or (not p) (not q) (not r))) (and p q r))
)
(push)
(assert (not exp))
(check-sat)
(get-model)
(pop)
(assert exp)
(check-sat)
(get-model)

; 5 - C
(declare-const p Bool)
(declare-const q Bool)

(define-fun exp() Bool
    (not (and (or (not p) q) (or p (not q))))
)
(push)
(assert (not exp))
(check-sat)
(get-model)
(pop)
(assert exp)
(check-sat)
(get-model)

; 6 - C
(declare-const p Bool)
(declare-const q Bool)

(define-fun exp() Bool
    (not (or (and p q) (and (not p) (not q))))
)

(push)
(assert (not exp))
(check-sat)
(get-model)
(pop)
(assert exp)
(check-sat)
(get-model)

; 7 - A, B (cba checking further)

(declare-const p Bool)

(define-fun exp() Bool
    (or (not p) p)
)
(push)
(assert (=> exp exp))
(check-sat)
(get-model)
(pop)
(assert (=> (and p and (not p)) exp))
(check-sat)
(get-model)