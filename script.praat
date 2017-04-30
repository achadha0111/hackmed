sound$ = "rec_1s"
sound = Read from file: sound$ + ".wav"

pitch = To Pitch (cc)... 0.01 50 15 no 0.03 0.45 0.01 0.35 0.14 300

selectObject: sound, pitch
pulses = To PointProcess (cc)

selectObject: sound, pulses, pitch
voiceReport$ = Voice report... 0 0 50 300 1.3 1.6 0.03 0.45

#writeInfoLine: voiceReport$

writeInfoLine: extractNumber(voiceReport$, "Jitter (local):")
writeInfoLine: extractNumber(voiceReport$, "Jitter (local, absolute):")
writeInfoLine: extractNumber(voiceReport$, "Jitter (rap):")
writeInfoLine: extractNumber(voiceReport$, "Jitter (ppq5):")
writeInfoLine: extractNumber(voiceReport$, "Jitter (ddp):")

writeInfoLine: extractNumber(voiceReport$, "Shimmer (local):")
writeInfoLine: extractNumber(voiceReport$, "Shimmer (local, dB):")
writeInfoLine: extractNumber(voiceReport$, "Shimmer (apq3):")
writeInfoLine: extractNumber(voiceReport$, "Shimmer (apq5):")
writeInfoLine: extractNumber(voiceReport$, "Shimmer (apq11):")
writeInfoLine: extractNumber(voiceReport$, "Shimmer (dda):")

writeInfoLine: extractNumber(voiceReport$, "Mean autocorrelation:")
writeInfoLine: extractNumber(voiceReport$, "Mean noise-to-harmonics ratio:")
writeInfoLine: extractNumber(voiceReport$, "Mean harmonics-to-noise ratio:")

writeInfoLine: extractNumber(voiceReport$, "Median pitch:")
writeInfoLine: extractNumber(voiceReport$, "Mean pitch:")
writeInfoLine: extractNumber(voiceReport$, "Standard deviation:")
writeInfoLine: extractNumber(voiceReport$, "Minimum pitch:")
writeInfoLine: extractNumber(voiceReport$, "Maximum pitch:")
writeInfoLine: extractNumber(voiceReport$, "Number of periods:")

writeInfoLine: extractNumber(voiceReport$, "Mean period:")
writeInfoLine: extractNumber(voiceReport$, "Standard deviation of period:")
writeInfoLine: extractNumber(voiceReport$, "Fraction of locally unvoiced frames:")

writeInfoLine: extractNumber(voiceReport$, "Number of voice breaks:")
writeInfoLine: extractNumber(voiceReport$, "Degree of voice breaks:")




removeObject: sound, pitch, pulses