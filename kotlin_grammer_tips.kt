// 빠른 입력받기 
val a = readln()

// decimal format
val df1 = DecimalFormat("00")
val df2 = DecimalFormat("##00.000")
val a = df1.format(6)
val b = df2.format(10000f)

// 공백으로 입력된 값 받기
val (x, y) = readln().split(" ").map { it.toInt() }

// n회 반복 간편하게
repeat(n) {

}

// 배열 선언
val intArray = IntArray(size = 3) // > [0, 0, 0] 
val intArrayOf = intArrayOf(0, 1, 2) // > [0, 1, 2] 지정한 값 대입
val intArrayAscending = IntArray(size = 3){ init -> init } // > [0, 1, 2]  
val intArrayTwice = IntArray(size = 3){ init -> init * 2} // > [0, 2, 4]

val immutableList: List<Int> = List(size = 3){ init -> init } // 불변 리스트 생성
val immutableListOf: List<Int> = listOf(1, 2, 3) // listOf() 메소드를 통해 리스트 생성

val mutableList: MutableList<Int> = MutableList(size = 3){ init -> init } // 가변 리스트 생성
val mutableListOf: MutableList<Int> = mutableListOf(1, 2, 3)

// Set 선언
val s = setOf(1, 2, 3)
val s = mutableSetOf(1, 2, 3)
val s = hashSetOf(1, 2, 3)
val s = sortedSetOf(1, 2, 3)
val s = linkedSetOf(1, 2, 3)

// set 메소드
s.contains(3)
s.add(4)
s.remove(1)
s.removeIf { it < 3 }

// MAP 선언
val m : MutableMap<String, String> = mutableMapOf("jinho" to "jaino", "simon" to "jiho")
val hashMap = HashMap<Int, String>()
val goal = "2"
hashMap.keys.forEach{
    if(hashMap.get(it) == goal){ // value에 접근하여 다른 조건식 적용
        return
    }
}

// MAP 메소드
m.put("a", "b")
m.remove("a")

// 2차원 배열
val charArrayInArray = arrayOf(
    charArrayOf('자', '이', '노'),
    charArrayOf('도', '미', '닉'),
) // > [['자', '이', '노'], ['도', '미', '닉']]

val intArrayInArray = Array(size = 3){ IntArray(size = 4){ init -> 2 } }

// 배열 메소드
lst.sumOf{ it.toInt() }
lst.minOf{ it.toInt() }
lst.maxOf{ it.toInt() }
lst.sort() // 오름차순 정렬 함수 
lst.sortDescending() // 내림차순 정렬 함수 
lst.forEach{ value -> println("index $value") } // 배열의 모든 값 순환 함수 
lst.forEachIndexed{ index, value -> println("index $index value $value") } // 배열의 모든 값, 인덱스 순환 함수
lst.filter{ index -> index == 0 } // 입력한 조건에 일치하는 값으로 구성된 리스트 반환 함수 
lst.sliceArray(IntRange(3, 9)) // 인덱스 범위에 따른 배열 반환 함수 
lst.slice(1 .. 3) // 인덱스 범위에 따른 리스트 반환 함수 
lst.sumOf{ index -> index * 2} // 조건을 적용한 모든 값 합 반환 함수 
lst.maxOrNull() // 최댓값, 크기가 없는 경우 null 반환 함수 
lst.minOrNull() // 최솟값, 크기가 없는 경우 null 반환 함수

lst.flatMap { listOf(it * 3, it * 4, it * 5) } // 모든 요소에 적용할 함수를 전달한다. 이때 함수의 반환값은 iterable(Collections을 포함하는 상위 객체)이여야 한다. 
lst.groupBy { it % 2 == 0 } // {false=[1, 3, 5], true=[2, 4]}
lst.add()
lst.remove()
lst.removeAt()
lst.addAll(lst2)

lst.distinct() // [1, 2, 3] 중복되는 값 제외 list
lst1.intersect(list2) // [3, 4, 5] 두 컬렉션 간 중첩되는 값 list 
lst1.union(list2) // [1, 2, 3, 4, 5, 6, 7] 중첩되는 값 소거 
lst1.plus(list2) // [1, 2, 3, 4, 5, 3, 4, 5, 6, 7] 중첩되는 값 소거 하지 않음

println(lst.contentToString()) // 배열의 모든 값 


// deque
val arrayDeque = ArrayDeque<Int>() // ArrayDeque 선언
val arrayDequeWithInitialList = ArrayDeque(listOf(1, 2, 3)) // 초기 값 대입 가능

arrayDeque.add(1) // 뒤에 1 추가
arrayDeque.addAll(listOf(2, 3, 4)) // 뒤에 리스트의 값 전부 추가

arrayDeque.addFirst(0) // 앞에 0 추가
arrayDeque.addLast(5) //  뒤에 5 추가. add() 와 같다.
// [0, 1, 2, 3, 4, 5]

arrayDeque.removeFirstOrNull() // 맨 앞 제거
arrayDeque.removeLastOrNull()


// 문자열 메소드
jainoString.length
jainoString.indices // 구성된 문자의 범위 반환 > 0 .. 13
jainoString.substring(startIndex = 1, endIndex =  3) // startIndex 와 endIndex 사이의 String 반환
jainoString.slice(1 .. 3) // 입력한 범위의 String 반환
jainoString.find{ char -> char == '안' } // 조건 식에 맞는 첫번째 문자 반환 
jainoString.filter{ char -> char == '안' } // 조건 식에 맞는 모든 문자를 합친 문자열 반환 
jainoString.replace(oldChar = '정', newChar = '김') // 문자 대치
jainoString.replace("a[bc]+d?".toRegex(), "") // 정규식 적용


// 정렬
list.sort() // 오름차순 정렬 > [1, 2, 3, 4, 5]
list.sortDescending() // 내림차순 정렬 > [5, 4, 3, 2, 1]
list.reverse() // 리스트 뒤집기 > [1, 2, 3, 4, 5]

list.sortBy{ int -> int % 3 } // > 정렬 기준을 입력하여, 정렬한다. 
println(list) // > [3, 1, 4, 2, 5] > 3으로 나눈 나머지의 오름차순 

list.sortWith(compareBy { int -> int % 2 }) // > Comparator 에 정의한 정렬 기준으로 정렬한다.
println(list) // > 4, 2, 3, 1, 5 > 2로 나눈 나머지의 오름차순 

list.sortWith(compareBy<Int> { init ->  init % 2 }.then(compareBy { int -> -int }))




// 시험 직전 꿀팁 /////////////////////////////////////////

// 1. 정렬

// 커스텀 비교
numbers.sortedBy{ ... }
numbers.sortedWith( compareBy<T>{ ... }.then( compareBy{ ... } ) )

// 둘 직접 비교
numbers.sortedWith(
    Comparator{ a, b -> 
        val c = (a.toString()+b.toString()).toInt()
        val d = (b.toString()+a.toString()).toInt()
        d.compareTo(c) 
    }
)