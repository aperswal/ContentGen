import AI_Creator as AI
from datetime import date

class Product:
    def __init__(self, product_name, product_description, product_price, product_affiliate_link):
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_affiliate_link = product_affiliate_link

class Marketing:
    def __init__(self):
        pass
        
class WrittenWord(Marketing):
    def __init__(self, product, type, word_limit, reading_comprehension):
        super().__init__()
        self.product = product
        self.type = self.set_type(type)
        self.word_limit = self.set_word_limit(word_limit)
        self.reading_comprehension = self.set_reading_comprehension(reading_comprehension)
        
    def get_type(self):
        return self.type
    
    def get_word_limit(self):
        return self.word_limit
    
    def get_reading_comprehension(self):
        return self.reading_comprehension
    
    def set_type(self, type):
        valid_types = ["Blog", "Book", "Article"]
        if type in valid_types:
            return type
        else:
            raise ValueError("Invalid type. Please enter 'Blog', 'Book', or 'Article'.")
            
    def set_word_limit(self, word_limit):
        if self.type == "Blog" and 500 <= word_limit <= 1500:
            return word_limit
        elif self.type == "Article" and 6000 <= word_limit <= 10000:
            return word_limit
        elif self.type == "Book" and 40000 <= word_limit <= 110000:
            return word_limit
        else:
            raise ValueError("Invalid word limit for the chosen type.")
    
    def set_reading_comprehension(self, reading_comprehension):
        valid_grades = ["7th Grade", "8th Grade", "9th Grade"]
        if reading_comprehension in valid_grades:
            return reading_comprehension
        else:
            raise ValueError("Invalid reading comprehension level. Please choose among '7th Grade', '8th Grade', or '9th Grade'.")
    
    def goal(self):
        print(f'We need to write a {self.type} with a word limit of {self.word_limit} at a reading comprehension of {self.reading_comprehension} to sell {self.product.product_name} at ${(self.product.product_price):.2f} to make ${(self.product.product_price * 0.2):.2f}.')
        
class Blog(WrittenWord):
    def __init__(self, headline, byLine, date, banner, content, cta):
        super().__init__()
        self.headline = headline
        self.byLine = byLine
        self.date = date
        self.banner = banner
        self.content = content
        self.cta = cta
    
    def get_headline(self):
        return self.headline
    
    def get_byLine(self):
        return self.byLine
    
    def get_date(self):
        return self.date
    
    def get_banner(self):
        return self.banner
    
    def get_content(self):
        return self.content
    
    def get_cta(self):
        return self.cta
    
    def set_headline(self, headline):
        self.headline = headline
        
    def set_byLine(self, byLine):
        self.byLine = byLine
        
    def set_date(self, date):
        self.date = date
        
    def set_banner(self, banner):
        self.banner = banner
        
    def set_content(self, content):
        self.content = content
    
    def set_cta(self, cta):
        self.cta = cta
    
    def add_content(self, content):
        self.content.append(content)
        
    def remove_content(self, content):
        self.content.remove(content)
        
    def clear_content(self):
        self.content.clear()
        
def main():
    try:
        ortho_bed = Product("Ortho Bed", "Orthopedic Bed", 2000, "https://www.ortho-bed.com/")
        pet_hut_ortho_bed = WrittenWord(ortho_bed, "Blog", 500, "7th Grade")
        pet_hut_ortho_bed.goal()
        pet_hut_ortho_bed_blog = Blog("6 to 11 Words, List Based", "a made up byline of the author",date.today(), "banner image in the format of *** Image Details ***, targets the target demographic of the article along with supports the headline, basically give me a 5 word search to copy and paste to find the banner image online.", "brief, follows a made up personal annecdote or narrative that is punchy and interesting and lead to a hook. Introduction should be no more than 4 sentences", "Then give me a line break then give me the list items in the following manner. Topic Overview (2 to 3 sentences), Ideal Image details similar to banner surrounded by *** Image 5 word search *** then description of the product, going from emotional to logical.","call to action, follow this formula for each list item. M-A-G-I-C Naming Formula: Magnetic Reason, Avatar, Goal, Time Interval, Container Word. Examples such as 88% Off 12-Week Bikini Blueprint, 60 Minute Make Your Friends Jealous Model Hair System, Bend Over Pain Free in 42 Days . . . Healing Fast Track")
        
    except ValueError as e:
        print(e)
        

if __name__ == "__main__":
    main()
