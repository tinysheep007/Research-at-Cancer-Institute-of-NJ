getwd()
setwd("../../../../")
setwd("/Code")
# read data
amp_data <- read.csv("./Rpractice/circos/amp.csv", header = TRUE)[, c(1:3, 9)]
del_data <- read.csv("./Rpractice/circos/del.csv", header = TRUE)[, 1:3]
head(amp_data)
head(del_data)

chromosome_vector <- amp_data$Chromosome
start_vector <- amp_data$Wide.peak.start
end_vector <- amp_data$Wide.peak.end
amp_logQ <- log10(amp_data$q.values)

print(chromosome_vector)
print(start_vector)
print(end_vector)
print(amp_logQ)

chromosome_vector_del <- del_data$Chromosome
start_vector_del <- del_data$Wide.peak.start
end_vector_del <- del_data$Wide.peak.end

# Printing the vectors
print(chromosome_vector_del)
print(start_vector_del)
print(end_vector_del)

# import circos library
library(circlize)

df = data.frame(
  chr = chromosome_vector,  # Example chromosome names
  start = start_vector,
  end = end_vector
 # qvalue = amp_logQ
)

df_amp_withQ = data.frame(
  chr = chromosome_vector,  # Example chromosome names
  start = start_vector,
  end = end_vector,
  value1 = amp_logQ
)

for (chr in unique(df_amp_withQ$chr)) {
  chr_data <- df_amp_withQ$value1[df_amp_withQ$chr == chr]
  if (length(unique(chr_data)) == 1) {
    cat("Chromosome", chr, "has a data range of 0. Check your data.\n")
  }
}

circos.par(cell.padding = c(0.02, 0, 0.02, 0))

# Filter out chromosomes with zero range in amp_logQ
df_filtered = df_amp_withQ[!(df_amp_withQ$chr %in% c('chr15', 'chr22')),]

# Proceed with the Circos plot initialization using the filtered data
circos.initialize(df_filtered$chr, x = df_filtered$value1)

circos.trackHist(df_filtered$chr, x = df_filtered$value1,bin.size = 1, col = "#999999", border = "#999999")

circos.track(df_filtered$chr, panel.fun = function(x, y) {
  sector.name <- CELL_META$sector.index
  # Using CELL_META$ylim to get the current sector's ylim, which helps position the text
  ylim <- CELL_META$ylim
  circos.text(CELL_META$xcenter, ylim[1], sector.name, facing = "clockwise", niceFacing = TRUE, adj = c(0, 0.5))
}, bg.border = NA, ylim = c(0, 1))  # Dummy ylim just to satisfy the function's requirement


print(df_filtered$chr)

summary(df_filtered$value1)
circos.clear()


df_del = data.frame(
  chr = chromosome_vector_del,  # Example chromosome names
  start = start_vector_del,
  end = end_vector_del 
)

bg_colors <- rep("#fc1303", nrow(df))

# Initialize the circos plot
circos.par(gap.degree = 5)
circos.genomicInitialize(df)
circos.track(ylim = c(0, 1), 
             bg.col = bg_colors, 
             bg.border = NA, track.height = 0.05)


length(df$chr) 
length(df_amp_withQ$qvalue)
summary(df_amp_withQ$qvalue)
sum(is.na(df_amp_withQ$qvalue))  # Should be 0
sum(is.infinite(df_amp_withQ$qvalue))  # Should be 0

qvalue_df <- data.frame(qvalue = df_amp_withQ$qvalue)


text(0, 0, "Amplified Gene = 90", cex = 1)
circos.info()
circos.clear()

# Initialize the circos plot with genomic data
circos.initializeWithIdeogram()
bg_colors <- rep("blue", nrow(df_del))
circos.genomicInitialize(df_del)
circos.track(ylim = c(0, 1), 
             bg.col = bg_colors, 
             bg.border = NA, track.height = 0.05)

circos.clear()
