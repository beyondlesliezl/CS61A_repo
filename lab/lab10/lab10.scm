(define (over-or-under num1 num2)
  'YOUR-CODE-HERE
(cond
  ((> num1 num2) 1)
  ((< num1 num2) -1)
  (else 0))
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0


;(define (filter-lst fn lst)
;  'YOUR-CODE-HERE
;)
(define (filter-lst fn lst)
(if (null? lst) nil
    (if (fn (car lst))
        (cons (car lst) (filter-lst fn (cdr lst)))
        (filter-lst fn (cdr lst)))))

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)


(define (make-adder num)
  'YOUR-CODE-HERE
  (lambda (new_num) (+ new_num num))
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13


(define lst
(cons (cons 1 nil) (cons 2 (cons
                              (cons 3 (cons 4 nil))
                              (cons 5 nil)))))


(define (composed f g)
  'YOUR-CODE-HERE
  (lambda (x) (f (g x))))


(define (remove item lst)
(if (null? lst) nil
    (if (= item (car lst))
        (remove item (cdr lst))
        (cons (car lst) (remove item (cdr lst))))))


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-reapeats item lst)
  (if (null? s) nil
      (cons (car s) (no-reapeats (remove (car s) (cdr s))))))

;(define (substitute s old new)
  ;(if (null? s)
      ;nil
      ;(if (pair? (car s))
                 ;(cons (substitute (car s) old new) (substitute (cdr s) old new))
          ;(if (list? (car s))

            ;(if (equal? (list old) (car s))
                ;(cons (list new) (substitute (cdr s) old new))
                ;(cons (list (car s)) (substitute (cdr s) old new))
            ;)
            ;(if (equal? old (car s))
                ;(cons new (substitute (cdr s) old new))
                ;(cons (car s) (substitute (cdr s) old new))
            ;)
        ;)
    ;)
;)
;)


(define (substitute s old new)
(cond
  ((null? s) nil)
  ((pair? s)
     (cons (substitute (car s) old new)
           (substitute (cdr s) old new)))
  ((equal? old s) new)
  (else s)
)
)
;很聪明，就是把所有的问题转化为对第一个的处理，也就是最基础的情况，而上面的pair就是处理是list的情况
(define (sub-all a olds news)
(if (null? olds)
    a
    (sub-all (substitute a (car olds) (car news))
             (cdr olds) (cdr news))))

(sub-all '(go ((bears))) '(go bears) '(big game))