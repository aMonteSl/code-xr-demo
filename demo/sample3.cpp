#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <memory>
#include <cmath>

// Simple class - Low complexity
class Point {
private:
    double x, y;

public:
    Point(double x = 0, double y = 0) : x(x), y(y) {}
    
    double getX() const { return x; }
    double getY() const { return y; }
    
    double distanceTo(const Point& other) const {
        double dx = x - other.x;
        double dy = y - other.y;
        return sqrt(dx * dx + dy * dy);
    }
};

// Medium complexity class
class Shape {
protected:
    std::string name;
    std::vector<Point> vertices;

public:
    Shape(const std::string& name) : name(name) {}
    virtual ~Shape() = default;
    
    virtual double area() const = 0;
    virtual double perimeter() const = 0;
    
    void addVertex(const Point& p) {
        vertices.push_back(p);
    }
    
    std::string getName() const { return name; }
    size_t getVertexCount() const { return vertices.size(); }
};

// High complexity class
class GeometryProcessor {
private:
    std::vector<std::unique_ptr<Shape>> shapes;
    std::map<std::string, int> shapeTypeCount;

public:
    void addShape(std::unique_ptr<Shape> shape) {
        if (shape) {
            std::string typeName = shape->getName();
            shapeTypeCount[typeName]++;
            shapes.push_back(std::move(shape));
        }
    }
    
    // Complex analysis function
    std::string analyzeCollection() const {
        if (shapes.empty()) {
            return "No shapes to analyze";
        }
        
        std::string analysis = "=== GEOMETRY ANALYSIS ===\n";
        
        double totalArea = 0;
        double totalPerimeter = 0;
        double maxArea = 0;
        double minArea = std::numeric_limits<double>::max();
        std::string largestShape, smallestShape;
        
        for (const auto& shape : shapes) {
            double area = shape->area();
            double perimeter = shape->perimeter();
            
            totalArea += area;
            totalPerimeter += perimeter;
            
            if (area > maxArea) {
                maxArea = area;
                largestShape = shape->getName();
            }
            
            if (area < minArea) {
                minArea = area;
                smallestShape = shape->getName();
            }
        }
        
        analysis += "Total Shapes: " + std::to_string(shapes.size()) + "\n";
        analysis += "Total Area: " + std::to_string(totalArea) + "\n";
        analysis += "Total Perimeter: " + std::to_string(totalPerimeter) + "\n";
        analysis += "Average Area: " + std::to_string(totalArea / shapes.size()) + "\n";
        analysis += "Largest Shape: " + largestShape + " (Area: " + std::to_string(maxArea) + ")\n";
        analysis += "Smallest Shape: " + smallestShape + " (Area: " + std::to_string(minArea) + ")\n";
        
        analysis += "\nShape Type Distribution:\n";
        for (const auto& [type, count] : shapeTypeCount) {
            double percentage = (static_cast<double>(count) / shapes.size()) * 100;
            analysis += "  " + type + ": " + std::to_string(count) + 
                       " (" + std::to_string(percentage) + "%)\n";
        }
        
        return analysis;
    }
    
    // Complex sorting and filtering
    std::vector<Shape*> getShapesByAreaRange(double minArea, double maxArea) const {
        std::vector<Shape*> filtered;
        
        for (const auto& shape : shapes) {
            double area = shape->area();
            if (area >= minArea && area <= maxArea) {
                filtered.push_back(shape.get());
            }
        }
        
        // Sort by area (descending)
        std::sort(filtered.begin(), filtered.end(), 
                 [](const Shape* a, const Shape* b) {
                     return a->area() > b->area();
                 });
        
        return filtered;
    }
};

// Concrete shape implementations
class Rectangle : public Shape {
private:
    double width, height;

public:
    Rectangle(double w, double h) : Shape("Rectangle"), width(w), height(h) {}
    
    double area() const override {
        return width * height;
    }
    
    double perimeter() const override {
        return 2 * (width + height);
    }
};

class Circle : public Shape {
private:
    double radius;

public:
    Circle(double r) : Shape("Circle"), radius(r) {}
    
    double area() const override {
        return 3.14159 * radius * radius;
    }
    
    double perimeter() const override {
        return 2 * 3.14159 * radius;
    }
};

int main() {
    GeometryProcessor processor;
    
    processor.addShape(std::make_unique<Rectangle>(5.0, 3.0));
    processor.addShape(std::make_unique<Circle>(2.5));
    processor.addShape(std::make_unique<Rectangle>(8.0, 4.0));
    processor.addShape(std::make_unique<Circle>(1.5));
    
    std::cout << processor.analyzeCollection() << std::endl;
    
    return 0;
}