(define/contract (is-palindrome x)
  (-> exact-integer? boolean?)
  (local [(define (loop n reversed-n)
            (if (= n 0)
            reversed-n
            (loop (quotient n 10) ; Get the rest of the number
              (+ (* reversed-n 10) (remainder n 10)))))] ; Add the last digit to reversed
  (if (< x 0)
      #false ; Handle negative numbers
      (= x (loop x 0))))
  )
