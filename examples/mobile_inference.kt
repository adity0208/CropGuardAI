val interpreter = Interpreter(loadModelFile(context, "animal_classifier_fp16.tflite"))

// Prepare input
val input = Array(1) { Array(160) { Array(160) { FloatArray(3) } } }

// Run inference
val output = Array(1) { FloatArray(7) }
interpreter.run(input, output)


val predictedClass = output[0].indices.maxByOrNull { output[0][it] } ?: 0
val confidence = output[0][predictedClass] * 100