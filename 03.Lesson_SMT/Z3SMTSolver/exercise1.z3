(declare-const green_ball Int)
(declare-const green_square Int)
(declare-const red_triangle Int)
(assert (= (+ green_ball green_ball) 10))
(assert (= (+ green_square (* green_ball green_square)) 12))
(assert (= (- (* green_ball green_square) (* red_triangle green_ball)) green_ball))
(check-sat)
(get-model)

; sat
; (
;   (define-fun green_ball () Int
;     5)
;   (define-fun red_triangle () Int
;     1)
;   (define-fun green_square () Int
;     2)
; )