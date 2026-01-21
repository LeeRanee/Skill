# Cloud Architecture Icons

## Overview

Draw.io has built-in support for cloud provider icons (AWS, Azure, GCP). Use `shape=mxgraph.aws4.*`, `shape=mxgraph.azure.*`, or `shape=mxgraph.gcp2.*` in the style attribute.

## AWS Icons

### Common AWS Services

**EC2 Instance:**
```xml
<mxCell id="2" value="EC2" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.ec2;" vertex="1" parent="1">
  <mxGeometry x="200" y="100" width="78" height="78" as="geometry"/>
</mxCell>
```

**S3 Bucket:**
```xml
<mxCell id="3" value="S3" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#7AA116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;" vertex="1" parent="1">
  <mxGeometry x="400" y="100" width="78" height="78" as="geometry"/>
</mxCell>
```

**Lambda Function:**
```xml
<mxCell id="4" value="Lambda" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lambda;" vertex="1" parent="1">
  <mxGeometry x="600" y="100" width="78" height="78" as="geometry"/>
</mxCell>
```

**RDS Database:**
```xml
<mxCell id="5" value="RDS" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;" vertex="1" parent="1">
  <mxGeometry x="200" y="250" width="78" height="78" as="geometry"/>
</mxCell>
```

**API Gateway:**
```xml
<mxCell id="6" value="API Gateway" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#E7157B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;" vertex="1" parent="1">
  <mxGeometry x="400" y="250" width="78" height="78" as="geometry"/>
</mxCell>
```

### AWS Service Categories

**Compute (Orange #ED7100):**
- `resIcon=mxgraph.aws4.ec2` - EC2
- `resIcon=mxgraph.aws4.lambda` - Lambda
- `resIcon=mxgraph.aws4.elastic_beanstalk` - Elastic Beanstalk
- `resIcon=mxgraph.aws4.ecs` - ECS
- `resIcon=mxgraph.aws4.eks` - EKS

**Storage (Green #7AA116):**
- `resIcon=mxgraph.aws4.s3` - S3
- `resIcon=mxgraph.aws4.efs` - EFS
- `resIcon=mxgraph.aws4.glacier` - Glacier

**Database (Purple #C925D1):**
- `resIcon=mxgraph.aws4.rds` - RDS
- `resIcon=mxgraph.aws4.dynamodb` - DynamoDB
- `resIcon=mxgraph.aws4.elasticache` - ElastiCache

**Networking (Purple #E7157B):**
- `resIcon=mxgraph.aws4.vpc` - VPC
- `resIcon=mxgraph.aws4.route_53` - Route 53
- `resIcon=mxgraph.aws4.cloudfront` - CloudFront
- `resIcon=mxgraph.aws4.elastic_load_balancing` - ELB
- `resIcon=mxgraph.aws4.api_gateway` - API Gateway

**Security (Red #DD344C):**
- `resIcon=mxgraph.aws4.iam` - IAM
- `resIcon=mxgraph.aws4.cognito` - Cognito
- `resIcon=mxgraph.aws4.secrets_manager` - Secrets Manager

## Azure Icons

### Common Azure Services

**Virtual Machine:**
```xml
<mxCell id="7" value="VM" style="aspect=fixed;html=1;points=[];align=center;image;fontSize=12;image=img/lib/azure2/compute/Virtual_Machine.svg;" vertex="1" parent="1">
  <mxGeometry x="200" y="400" width="68" height="62" as="geometry"/>
</mxCell>
```

**Storage Account:**
```xml
<mxCell id="8" value="Storage" style="aspect=fixed;html=1;points=[];align=center;image;fontSize=12;image=img/lib/azure2/storage/Storage_Accounts.svg;" vertex="1" parent="1">
  <mxGeometry x="400" y="400" width="68" height="54" as="geometry"/>
</mxCell>
```

**SQL Database:**
```xml
<mxCell id="9" value="SQL DB" style="aspect=fixed;html=1;points=[];align=center;image;fontSize=12;image=img/lib/azure2/databases/SQL_Database.svg;" vertex="1" parent="1">
  <mxGeometry x="600" y="400" width="68" height="68" as="geometry"/>
</mxCell>
```

### Azure Service Paths

- Virtual Machine: `img/lib/azure2/compute/Virtual_Machine.svg`
- App Service: `img/lib/azure2/app_services/App_Services.svg`
- Functions: `img/lib/azure2/compute/Function_Apps.svg`
- Storage: `img/lib/azure2/storage/Storage_Accounts.svg`
- SQL Database: `img/lib/azure2/databases/SQL_Database.svg`
- Cosmos DB: `img/lib/azure2/databases/Azure_Cosmos_DB.svg`
- Virtual Network: `img/lib/azure2/networking/Virtual_Networks.svg`
- Load Balancer: `img/lib/azure2/networking/Load_Balancers.svg`
- API Management: `img/lib/azure2/app_services/API_Management_Services.svg`

## GCP Icons

### Common GCP Services

**Compute Engine:**
```xml
<mxCell id="10" value="Compute Engine" style="sketch=0;html=1;verticalAlign=top;labelPosition=center;verticalLabelPosition=bottom;align=center;spacingTop=-6;fontSize=11;fontStyle=1;fontColor=#999999;shape=mxgraph.gcp2.compute_engine;" vertex="1" parent="1">
  <mxGeometry x="200" y="550" width="75" height="75" as="geometry"/>
</mxCell>
```

**Cloud Storage:**
```xml
<mxCell id="11" value="Cloud Storage" style="sketch=0;html=1;verticalAlign=top;labelPosition=center;verticalLabelPosition=bottom;align=center;spacingTop=-6;fontSize=11;fontStyle=1;fontColor=#999999;shape=mxgraph.gcp2.cloud_storage;" vertex="1" parent="1">
  <mxGeometry x="400" y="550" width="75" height="75" as="geometry"/>
</mxCell>
```

**Cloud SQL:**
```xml
<mxCell id="12" value="Cloud SQL" style="sketch=0;html=1;verticalAlign=top;labelPosition=center;verticalLabelPosition=bottom;align=center;spacingTop=-6;fontSize=11;fontStyle=1;fontColor=#999999;shape=mxgraph.gcp2.cloud_sql;" vertex="1" parent="1">
  <mxGeometry x="600" y="550" width="75" height="75" as="geometry"/>
</mxCell>
```

### GCP Service Shapes

- Compute Engine: `shape=mxgraph.gcp2.compute_engine`
- Cloud Functions: `shape=mxgraph.gcp2.cloud_functions`
- Cloud Run: `shape=mxgraph.gcp2.cloud_run`
- Cloud Storage: `shape=mxgraph.gcp2.cloud_storage`
- Cloud SQL: `shape=mxgraph.gcp2.cloud_sql`
- BigQuery: `shape=mxgraph.gcp2.bigquery`
- Pub/Sub: `shape=mxgraph.gcp2.cloud_pubsub`
- Cloud Load Balancing: `shape=mxgraph.gcp2.load_balancing`
- VPC Network: `shape=mxgraph.gcp2.virtual_private_cloud`

## Generic Cloud Icons

For cloud-agnostic diagrams:

**Generic Server:**
```xml
<mxCell id="13" value="Server" style="image;html=1;image=img/lib/clip_art/computers/Server_128x128.png" vertex="1" parent="1">
  <mxGeometry x="200" y="700" width="80" height="80" as="geometry"/>
</mxCell>
```

**Generic Database:**
```xml
<mxCell id="14" value="Database" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
  <mxGeometry x="400" y="700" width="80" height="100" as="geometry"/>
</mxCell>
```

**Generic Cloud:**
```xml
<mxCell id="15" value="Cloud Service" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="600" y="700" width="120" height="80" as="geometry"/>
</mxCell>
```

## User/Actor Icons

**User/Person:**
```xml
<mxCell id="16" value="User" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="30" height="60" as="geometry"/>
</mxCell>
```

**Multiple Users:**
```xml
<mxCell id="17" value="Users" style="verticalLabelPosition=bottom;html=1;verticalAlign=top;align=center;strokeColor=none;fillColor=#00BEF2;shape=mxgraph.azure.users;" vertex="1" parent="1">
  <mxGeometry x="100" y="250" width="47.5" height="50" as="geometry"/>
</mxCell>
```

## Architecture Diagram Tips

1. **Consistent Sizing**: Use 68-78px for most cloud icons
2. **Spacing**: Keep 100-150px between icons
3. **Grouping**: Use containers (rounded rectangles) for VPCs/Subnets
4. **Labels**: Place below icons (`verticalLabelPosition=bottom`)
5. **Connections**: Use `endArrow=classic` for data flow
6. **Color Coding**: Match provider colors (AWS orange, Azure blue, GCP colors)

## Example: Simple AWS Architecture

```xml
<mxCell id="2" value="User" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;" vertex="1" parent="1">
  <mxGeometry x="50" y="140" width="30" height="60" as="geometry"/>
</mxCell>

<mxCell id="3" value="CloudFront" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#E7157B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;" vertex="1" parent="1">
  <mxGeometry x="150" y="130" width="78" height="78" as="geometry"/>
</mxCell>

<mxCell id="4" value="S3" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#7AA116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;" vertex="1" parent="1">
  <mxGeometry x="300" y="130" width="78" height="78" as="geometry"/>
</mxCell>

<mxCell id="5" style="endArrow=classic;html=1;" edge="1" parent="1" source="2" target="3">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>

<mxCell id="6" style="endArrow=classic;html=1;" edge="1" parent="1" source="3" target="4">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```
