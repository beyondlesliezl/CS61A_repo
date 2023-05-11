(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))

)

(define (caddr s)
  (car (cdr (cdr s)))

)


(define (sign num)
  (cond
    ((< num 0) -1)
    ((> num 0) 1)
    ((= num 0) 0)
    )
)


(define (square x) (* x x))

(define (pow x y)
  (cond
    ((= y 2) (square x))
    ((even? y)
     (square
      (pow x (/ y 2))))

     ((odd? y)
      (* x (pow x (- y 1))))
  )
)



(define (unique s) 
(if (null? s) nil
    (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s)))))
)


(define (replicate x n)
  (define (repli-helper x n result)
    (if (= n 0)
        result
        (repli-helper x (- n 1) (cons x result))
    )
  )
  (repli-helper x n nil)
)

(define (accumulate combiner start n term)
(define (natu_num n term combiner result now_num)
  (if (= (- now_num 1) n)
      result
      (natu_num n term combiner
                (combiner (term now_num) result)
                (+ now_num 1)
      )
  )
)

(combiner start (natu_num n term combiner (term 1) 2))
)

(define (accumulate-tail combiner start n term)
(define (natu_num n term combiner result now_num)
  (if (= (- now_num 1) n)
      result
      (natu_num n term combiner
                (combiner (term now_num) result)
                (+ now_num 1)
      )
  )
)

(combiner start (natu_num n term combiner (term 1) 2))
)




(define-macro (list-of map-expr for var in lst if filter-expr)
`(map (lambda (,var) ,map-expr) (filter (lmabda (,var) ,filter-expr),lst))
)
