
(define-macro (def func args body)
  `(define ,(cons func args) ,body))


(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define all-three-multiples
 (map-stream (lambda (x) (+ x 3))
             (cons-stream 0 all-three-multiples)))



(define (compose-all funcs)
  (lambda (x)
    (cond
      ((null? funcs) x)
      (else
       ((compose-all (cdr funcs))
        ((car funcs) x))))))


(define (helper sum stream)
  (cond
    ((null? stream) nil)
    (else
     (cons-stream (+ sum (car stream))
                   (helper (+ sum (car stream)) (cdr-stream stream))))))

(define (partial-sums stream)
  (helper 0 stream)
)

