fun <T> T?.println() = kotlin.io.println(this)

fun main(args: Array<String>) {
    dog(Action.feed)(5)
}

val add = { a: Int, b: String -> "$a$b" }

fun <P1, P2, P3, R> Function3<P1, P2, P3, R>.curried()
        = fun(p1: P1) = fun(p2: P2) = fun(p3: P3) = this(p1, p2, p3)

fun <P1, P2, R> Function2<P1, P2, R>.curried()
        = fun(p1: P1) = fun(p2: P2) = this(p1, p2)

fun add(a: Int, b: Int, c: Int): Int {
    return a + b + c
}

fun <P1, P2, R> Function2<P1, P2, R>.partial1(p1: P1) = fun(p2: P2) = this(p1, p2)
fun <P1, P2, R> Function2<P1, P2, R>.partial2(p2: P2) = fun(p1: P1) = this(p1, p2)


val dog = { action: Action ->
    var weight = 10
    when (action) {
        Action.feed -> { food: Int -> weight += food; println(weight) }
        Action.workout -> { intensity: Int -> weight += intensity; println(weight) }
    }
}

enum class Action {
    feed, workout
}








