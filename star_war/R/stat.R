library(ggplot2)

films <- read.csv('../csv/stat_basic.csv',header=TRUE,sep=',')
ggplot(films) + geom_bar(aes(x=key, y=value, fill=title), position="dodge", stat="identity") + scale_fill_brewer(palette="Set2") + labs(x='', y='') + theme(legend.title=element_blank(),axis.text.x=element_text(size=15),axis.text.y=element_text(size=15),legend.text=element_text(size=15))

characters <- read.csv('../csv/stat_character.csv',header=TRUE,sep=',')
ggplot(characters) + geom_point(aes(x=mass, y=height, color=gender)) + scale_fill_brewer(palette="Set2") + theme(legend.title=element_blank(),axis.title.x=element_text(size=20),axis.text.x=element_text(size=15),axis.title.y=element_text(size=20),axis.text.y=element_text(size=15),legend.text=element_text(size=15))

species <- read.csv('../csv/stat_species.csv',header=TRUE,sep=',')
ggplot(species) + geom_point(aes(x=lifespan, y=height, color=classification)) + scale_fill_brewer(palette="Set2") + theme(legend.title=element_blank(),axis.title.x=element_text(size=20),axis.text.x=element_text(size=15),axis.title.y=element_text(size=20),axis.text.y=element_text(size=15),legend.text=element_text(size=15))
