
fun main(
    video_len: String, 
    pos: String, 
    op_start: String, 
    op_end: String, 
    commands: Array<String>
): String {
    val videoLen = 60*video_len.slice(0..1).toInt() + video_len.slice(3..4).toInt()
    val startPos = 60*pos.slice(0..1).toInt() + pos.slice(3..4).toInt()
    val opStart = 60*op_start.slice(0..1).toInt() + op_start.slice(3..4).toInt()
    val opEnd = 60*op_end.slice(0..1).toInt() + op_end.slice(3..4).toInt()
    
    var curPos = if(opStart<=startPos && startPos<opEnd) { opEnd } else { startPos }
    commands.forEach { command: String ->
        when(command) {
            "next" -> curPos = listOf(opEnd, curPos+10).min()
            "prev" -> curPos = listOf(0, curPos-10).max()
        }
    }
    val df = DecimalFormat("##")
    
    return "${df.format(curPos/60)}:${df.format(curPos%60)}"
}