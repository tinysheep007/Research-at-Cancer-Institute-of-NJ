getwd()
setwd("../../../../")
setwd("/Code")
amp_data <- read.csv("./Rpractice/circos/amp normalize.csv", header = FALSE)[, 1:4]
head(amp_data)

df = data.frame(
  chr = amp_data$V1,  # Example chromosome names
  start = amp_data$V2,
  end = amp_data$V3,
  qvalue = amp_data$V4
)

head(df)

library(circlize)



for (chr in unique(df$chr)) {
  chr_data <- df$qvalue[df$chr == chr]
  if (length(unique(chr_data)) == 1) {
    cat("Chromosome", chr, "has a data range of 0. Check your data.\n")
  }
}

circos.par(cell.padding = c(0.02, 0, 0.02, 0))

# Filter out chromosomes with zero range in amp_logQ
df_filtered = df[!(df$chr %in% c('chr15', 'chr22')),]

df_filtered = df_filtered[complete.cases(df_filtered$end), ]

df_filtered
# Proceed with the Circos plot initialization using the filtered data
circos.initialize(df_filtered$chr, x = df_filtered$qvalue)

circos.trackHist(df_filtered$chr, x = df_filtered$qvalue,bin.size = 1, col = "#999999", border = "#999999")

circos.trackHist(df_filtered$chr, x = df_filtered$qvalue, draw.density = TRUE, 
                 col = "#999999", border = "#999999")

circos.track(df_filtered$chr, panel.fun = function(x, y) {
  sector.name <- CELL_META$sector.index
  # Using CELL_META$ylim to get the current sector's ylim, which helps position the text
  ylim <- CELL_META$ylim
  circos.text(CELL_META$xcenter, ylim[1], sector.name, facing = "clockwise", niceFacing = TRUE, adj = c(0, 0.5))
}, bg.border = NA, ylim = c(0, 1))  # Dummy ylim just to satisfy the function's requirement


print(df_filtered$chr)

summary(df_filtered$qvalue)
circos.clear()
