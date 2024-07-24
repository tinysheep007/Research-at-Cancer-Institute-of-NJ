human_cytoband = read.cytoband(species = "hg19")$df
mouse_cytoband = read.cytoband(species = "mm10")$df

human_cytoband[ ,1] = paste0("human_", human_cytoband[, 1])
mouse_cytoband[ ,1] = paste0("mouse_", mouse_cytoband[, 1])

cytoband = rbind(human_cytoband, mouse_cytoband)
head(cytoband)

chromosome.index = c(paste0("human_chr", c(1:22, "X", "Y")), 
                     rev(paste0("mouse_chr", c(1:19, "X", "Y"))))
circos.clear()

circos.par(gap.after = c(rep(1, 23), 5, rep(1, 20), 5))
circos.initializeWithIdeogram(cytoband, plotType = NULL, 
                              chromosome.index = chromosome.index)
circos.track(ylim = c(0, 1), panel.fun = function(x, y) {
  circos.text(CELL_META$xcenter, CELL_META$ylim[2] + mm_y(2), 
              gsub(".*chr", "", CELL_META$sector.index), cex = 0.6, niceFacing = TRUE)
}, track.height = mm_h(1), cell.padding = c(0, 0, 0, 0), bg.border = NA)
highlight.chromosome(paste0("human_chr", c(1:22, "X", "Y")), 
                     col = "red", track.index = 1)
highlight.chromosome(paste0("mouse_chr", c(1:19, "X", "Y")), 
                     col = "blue", track.index = 1)

circos.genomicIdeogram(cytoband)
