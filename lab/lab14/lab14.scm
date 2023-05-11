
(define (split-at lst n)
(cond
((= n 0) (cons nil lst))
((null? lst) (cons nil nil))
(else
 (cons
  (cons (car lst) (car (split-at (cdr lst) (- n 1))))
  (cdr (split-at (cdr lst) (- n 1)))))))

;(define-macro (switch expr cases)
;	(cons _________
;		(map (_________ (_________) (cons _________ (cdr case)))
;    			cases))
;)

(define-macro (switch expr cases)
  (cons 'cond
	(map (lambda (case) (cons (eq? (eval expr) (car case))  (cdr case)))
			cases))
)